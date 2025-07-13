import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from usuarios.models import Usuario

stripe.api_key = settings.STRIPE_SECRET_KEY

def subscripcion(request):
    return render(request, 'subscripcion.html', {
        'stripe_key': settings.STRIPE_PUBLISHABLE_KEY
    })


def pagar_gratis(request):
    usuario = Usuario.objects.get(user=request.user)
    usuario.plan_actual = 'Gratis'
    usuario.save()
    return render(request, 'confirmacion.html', {'plan': 'Gratis'})


def crear_sesion_pago(request, tipo):
    precios = {
        'premium': 'prod_Sb7f2VUPoVuVUp',   # <- ID del producto en Stripe
        'empresas': 'prod_Sb7fZv2jDguRVA',
    }

    if tipo not in precios:
        return redirect('monetizacion:subscripcion')

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': precios[tipo],
            'quantity': 1,
        }],
        mode='subscription',
        success_url=settings.DOMAIN + f'/subscripciones/success/{tipo}/',
        cancel_url=settings.DOMAIN + '/subscripciones/cancel/',
        customer_email=request.user.email,
    )

    return redirect(session.url)

def pago_exitoso(request, tipo):
    usuario = Usuario.objects.get(user=request.user)
    usuario.plan_actual = tipo.capitalize()
    usuario.save()
    return render(request, 'confirmacion.html', {'plan': tipo.capitalize()})

def pago_cancelado(request):
    return render(request, 'cancelado.html')

from django.urls import path
from . import views

app_name = 'monetizacion'

urlpatterns = [
    path('', views.subscripcion, name='subscripcion'),
    path('pago/gratis/', views.pagar_gratis, name='pagar_gratis'),
    path('pago/<str:tipo>/', views.crear_sesion_pago, name='crear_pago'),
    path('subscripciones/success/<str:tipo>/', views.pago_exitoso, name='pago_exitoso'),
    path('subscripciones/cancel/', views.pago_cancelado, name='pago_cancelado'),
]

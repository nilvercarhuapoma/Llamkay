from django.core.exceptions import PermissionDenied
from functools import wraps

def rol_requerido(roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            try:
                tipo = user.perfil.tipo_usuario  # <-- acceso al modelo Usuario
            except Exception as e:
                print("ERROR en decorador:", e)
                raise PermissionDenied("No tienes permiso para acceder a esta vista.")

            print("DEBUG: tipo_usuario del perfil:", tipo)

            if tipo not in roles:
                raise PermissionDenied("No tienes permiso para acceder a esta vista.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator 

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            tipo = getattr(request.user, 'tipo_usuario', None)
            print(f"DEBUG: tipo_usuario actual = {tipo}")
            if tipo not in roles:
                raise PermissionDenied("No tienes permiso para acceder a esta vista.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


"""
URL configuration for llamkay project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from usuarios.views import oauth2callback, desconectar_google


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('trabajo_llamkay.urls')),

    path('usuarios/', include('usuarios.urls')),  
    path('trabajos/', include('trabajos.urls')),
    path('chats/', include('chats.urls')),
    
    #Google calendar
    path('oauth2callback/', oauth2callback, name='oauth_callback'),
    path('desconectar-google/', desconectar_google, name='desconectar_google'),


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""VeteriTec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from home import urls as home
from funcionarios import urls as funcionarios
from agenda import urls as agenda
from calculadora import urls as calculadora
from clientes import urls as clientes
from fornecedor import urls as fornecedor
from relatorio import urls as relatorio
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include(home)),
    path('funcionarios/', include(funcionarios)),
    path('agenda/', include(agenda)),
    path('calculadora/', include(calculadora)),
    path('clientes/', include(clientes)),
    path('fornecedor/', include(fornecedor)),
    path('relatorio/', include(relatorio)),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

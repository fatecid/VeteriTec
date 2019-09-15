from django.urls import path
from .views import relatorio
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', relatorio, name="relatorio"),

]
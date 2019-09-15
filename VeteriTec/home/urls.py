from django.urls import path
from .views import home, mylogout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', home, name="home"),
    path('logout/', mylogout, name="mylogout"),
]

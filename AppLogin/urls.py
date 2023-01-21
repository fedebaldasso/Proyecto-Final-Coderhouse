from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('', home, name="home"),
    
    path('login/', login_request, name="login"), #no le ponemos login solo porque ya existe "login" en Django
    path('logout/', LogoutView.as_view(), name="logout"), #no le ponemos login solo porque ya existe "login" en Django


]
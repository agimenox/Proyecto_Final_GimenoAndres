from django.urls import path
from login_app.views import *


urlpatterns = [

    
    path('home/', home, name="home"),
    #Usuario y sesion
    path('register/', user_register, name="register"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('login/', login_view, name="login"),
    path('about/', about, name="about"),

]
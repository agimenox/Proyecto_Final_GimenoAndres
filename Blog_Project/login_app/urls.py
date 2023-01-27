from django.urls import path
from login_app.views import *



urlpatterns = [

    
    path('home/', home, name="home"),
    #Usuario y sesion
    path('register/', user_register, name="register"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('login/', login_view, name="login"),
    path('about/', about, name="about"),
    #Perfil     
    path('edit-profile/', ProfileUpdateView.as_view(), name="editar_perfil"),
    #path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),

]


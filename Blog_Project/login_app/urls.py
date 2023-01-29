from django.urls import path
from login_app.views import *
from . import views



urlpatterns = [

    
    path('home/', home, name="home"),
    #User and Session
    path('accounts/signup/', user_register, name="register"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('login/', login_view, name="login"),
    path('about/', about, name="about"),
    #Profile    
    path('edit-profile/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('add-avatar/', views.add_avatar, name="add_avatar"),

]


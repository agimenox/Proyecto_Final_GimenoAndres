from django.urls import path
from login_app.views import *
from . import views



urlpatterns = [

    
    path('home/', home, name="home"),
    #User and Session
    path('accounts/signup/', user_register, name="register"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('accounts/login/', login_view, name="login"),
    path('about/', about, name="about"),
    #Profile    
    path('edit-profile/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('add-avatar/', views.add_avatar, name="add_avatar"),
    path('contact/', views.show_contact, name="show_contact"),
    path('list-users/', views.list_users, name="list_users"),
    path('delete-user/<int:id>', views.delete_user, name='delete_user'),

]


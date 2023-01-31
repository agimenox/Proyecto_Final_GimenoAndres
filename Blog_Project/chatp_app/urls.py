from django.urls import path
from . import views

urlpatterns = [
    path('home-chat/', views.home_chat, name='home_chat'),
    path('<str:room>/', views.room, name='room'),
    path('home-chat/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]
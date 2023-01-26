from django.urls import path
from blog_app.views import *
from .views import BlogCreateView, BlogListView, BlogUpdateView


urlpatterns = [

    path('create-blog/', BlogCreateView.as_view(), name="create_blog"),
    path('list-blogs/', BlogListView.as_view(), name="list_blogs"),
    path('update-blog/<int:pk>/', BlogUpdateView.as_view(), name="edit_blog"),

]
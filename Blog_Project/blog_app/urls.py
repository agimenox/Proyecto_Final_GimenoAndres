from django.urls import path
from blog_app.views import *
from .views import BlogCreateView, BlogListView, BlogUpdateView, BlogDeleteView, BlogDetailView

urlpatterns = [

    path('create-blog/', BlogCreateView.as_view(), name="create_blog"),
    path('pages/', BlogListView.as_view(), name="list_blogs"),
    path('update-blog/<int:pk>/', BlogUpdateView.as_view(), name="edit_blog"),
    path('delete-blog/<int:pk>/', BlogDeleteView.as_view(), name="delete_blog"),
    path('pages/<int:pk>/', BlogDetailView.as_view(), name="detail_blog"),

]
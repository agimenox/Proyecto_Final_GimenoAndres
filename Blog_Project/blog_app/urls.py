from django.urls import path
from .views import BlogCreateView, BlogListView, BlogUpdateView, BlogDeleteView, BlogDetailView
from . import views

urlpatterns = [

    path('create-blog/', BlogCreateView.as_view(), name="create_blog"),
    path('pages/', BlogListView.as_view(), name="list_blogs"),
    path('update-blog/<int:pk>/', BlogUpdateView.as_view(), name="edit_blog"),
    path('delete-blog/<int:pk>/', BlogDeleteView.as_view(), name="delete_blog"),
    path('pages/<int:pk>/', BlogDetailView.as_view(), name="detail_blog"),
    path('own-blogs/<int:id>/',views.get_own_blog, name="own_blogs"),


]
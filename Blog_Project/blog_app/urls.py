from django.urls import path
from blog_app.views import *
from .views import BlogCreateView, BlogListView


urlpatterns = [

    path('create-blog/', BlogCreateView.as_view(), name="create_blog"),
    path('list-blogs/', BlogListView.as_view(), name="list_blogs"),

]
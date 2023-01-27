from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog_app.models import Blog
from django.urls import reverse, reverse_lazy

# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'subtitle','body','author','date','image','category']
    success_url = reverse_lazy('list_blogs')
    template_name = "create_blog.html"

class BlogListView(ListView):
    model = Blog
    template_name = 'list_blogs.html'

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'subtitle','body','author','date','image','category']
    success_url = reverse_lazy('list_blogs')
    template_name = "edit_blog.html"

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('list_blogs')
    template_name = "confirm_blog_elimination.html"

class BlogDetailView(DetailView):
    model = Blog
    success_url = reverse_lazy('list_blogs')
    template_name = "detail_blog.html"
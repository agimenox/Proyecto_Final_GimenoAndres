from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog_app.models import Blog
from django.urls import reverse, reverse_lazy

# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'subtitle','body','author','date','image','category']
    success_url = reverse_lazy('list_blogs')
    template_name = "create_blog.html"

def list_blogs(request):
    object_list = {
        'blogs': Blog.objects.all()
    }
    return render(
        request=request,
        template_name='list_blogs.html',
        context=object_list,
    )

class BlogListView(ListView):
    model = Blog
    template_name = 'list_blogs.html'
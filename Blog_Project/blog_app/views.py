from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from blog_app.models import Blog
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    fields = ['title', 'subtitle','body','author','date','image','category',]
    success_url = reverse_lazy('list_blogs')
    template_name = "create_blog.html"
    
    def form_valid(self, form):
        Blog = form.save(commit=False)
        Blog.owner = self.request.user
        #article.save()  # This is redundant, see comments.
        return super(BlogCreateView, self).form_valid(form)

class BlogListView(ListView):
    model = Blog
    template_name = 'list_blogs.html'

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ['title', 'subtitle','body','author','date','image','category']
    success_url = reverse_lazy('list_blogs')
    template_name = "edit_blog.html"

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Blog
    success_url = reverse_lazy('list_blogs')
    template_name = "confirm_blog_elimination.html"

class BlogDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    redirect_field_name = 'list_blogs'
    model = Blog
    success_url = reverse_lazy('list_blogs')
    template_name = "detail_blog.html"

def get_own_blog(request,id):
    form = Blog.objects.filter(owner_id=id)
    return render(
        request=request,
        template_name='list_own_blogs.html',
        context={'form': form},
    )

def get_all_blog(request):
    contx = Blog.objects.all()
    return render(
        request=request,
        template_name='list_all_blogs.html',
        context={'form': contx},
    )

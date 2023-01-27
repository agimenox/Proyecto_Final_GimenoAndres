
from django import forms
from blog_app.models import Blog


class BlogCreateForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'subtitle','body','author','date','image','category','owner']

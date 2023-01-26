
from django import forms
from models import Blog


class BlogCreateForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'subtitle','body','author','date','image','category']
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=128)
    body = models.TextField(max_length=1024)
    author = models.CharField(max_length=64)
    date = models.DateField()
    image = models.ImageField(upload_to='blogs', null=True, blank=True)
    category = models.CharField(max_length=64,null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Imagen del Blog: {self.title}'


# Create your models here.

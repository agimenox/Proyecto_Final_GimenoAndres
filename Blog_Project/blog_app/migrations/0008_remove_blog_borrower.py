# Generated by Django 4.1.5 on 2023-01-27 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_blog_borrower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='borrower',
        ),
    ]

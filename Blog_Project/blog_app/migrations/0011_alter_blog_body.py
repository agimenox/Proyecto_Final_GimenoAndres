# Generated by Django 4.1.5 on 2023-01-30 17:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_rename_borrower_blog_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(max_length=1024),
        ),
    ]

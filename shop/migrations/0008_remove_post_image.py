# Generated by Django 3.0 on 2020-10-05 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]

# Generated by Django 3.0 on 2020-10-05 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]

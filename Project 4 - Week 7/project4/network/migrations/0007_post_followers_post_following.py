# Generated by Django 4.2.1 on 2023-06-11 19:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_alter_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='followers',
            field=models.ManyToManyField(related_name='subs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='following',
            field=models.ManyToManyField(related_name='subbing', to=settings.AUTH_USER_MODEL),
        ),
    ]

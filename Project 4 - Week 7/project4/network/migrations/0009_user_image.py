# Generated by Django 4.2.1 on 2023-06-11 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_remove_post_followers_remove_post_following_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.URLField(blank=True, max_length=9999, null=True),
        ),
    ]

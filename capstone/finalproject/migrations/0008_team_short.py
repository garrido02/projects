# Generated by Django 4.2.1 on 2023-06-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproject', '0007_team_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='short',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-29 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalproject', '0008_team_short'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='desc1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pack',
            name='desc2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pack',
            name='desc3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pack',
            name='desc4',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pack',
            name='desc5',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pack',
            name='desc6',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.2.12 on 2023-05-19 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(default='', max_length=100),
        ),
    ]
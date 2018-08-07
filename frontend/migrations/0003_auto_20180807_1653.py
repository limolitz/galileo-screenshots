# Generated by Django 2.1 on 2018-08-07 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_screenshot_screenshot_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='request_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenshot',
            name='screenshot_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='screenshot',
            name='user_agent',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='screenshot_name',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='url',
            field=models.URLField(),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-24 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0010_alter_click_created_on_alter_view_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advetiser',
            name='clicks',
        ),
        migrations.RemoveField(
            model_name='advetiser',
            name='views',
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0008_alter_view_user_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='created_on',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='view',
            name='created_on',
            field=models.DateTimeField(),
        ),
    ]

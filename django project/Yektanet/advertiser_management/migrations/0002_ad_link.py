# Generated by Django 5.0.2 on 2024-02-22 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='link',
            field=models.CharField(default='', max_length=200),
        ),
    ]

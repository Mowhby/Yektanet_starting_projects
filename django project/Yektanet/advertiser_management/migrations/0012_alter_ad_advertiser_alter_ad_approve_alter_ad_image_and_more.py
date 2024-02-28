# Generated by Django 5.0.2 on 2024-02-26 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0011_remove_advetiser_clicks_remove_advetiser_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='advertiser',
            field=models.ForeignKey(help_text='Advertiser who created this ad.', on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.advetiser'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='approve',
            field=models.BooleanField(default=False, help_text='Each ad must be approved by the admin before being shown.'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(help_text='image of the ad should be added in this part.', upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='click',
            name='ad',
            field=models.ForeignKey(help_text='What ad was clicked on.', on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.ad'),
        ),
        migrations.AlterField(
            model_name='view',
            name='ad',
            field=models.ForeignKey(help_text='What ad has been viewed.', on_delete=django.db.models.deletion.CASCADE, to='advertiser_management.ad'),
        ),
    ]

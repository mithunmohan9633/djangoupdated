# Generated by Django 5.1.2 on 2024-11-04 04:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_remove_carforrent_created_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carforrent',
            name='car_image',
        ),
        migrations.AddField(
            model_name='carforrent',
            name='rent_car_image',
            field=models.ImageField(default='No image', upload_to='car_images/rent_car_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carforrent',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),

            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='brand',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='mileage',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='oil_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='registration_number',
            field=models.CharField(max_length=255),
        ),
    ]

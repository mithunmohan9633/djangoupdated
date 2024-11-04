# Generated by Django 5.1.2 on 2024-11-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_remove_carforrent_created_date_and_more'),  # Ensure this is the correct dependency
    ]

    operations = [
        migrations.AlterField(
            model_name='carforrent',
            name='registration_number',
            field=models.CharField(max_length=50),  # Updated as needed
        ),
        migrations.AlterField(
            model_name='carforrent',
            name='whatsapp_number',
            field=models.CharField(max_length=50),  # Updated max_length for WhatsApp number
        ),
    ]

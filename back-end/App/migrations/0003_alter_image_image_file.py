# Generated by Django 4.1.2 on 2023-08-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to='image/'),
        ),
    ]

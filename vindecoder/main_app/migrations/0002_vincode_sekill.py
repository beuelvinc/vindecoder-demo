# Generated by Django 2.2.5 on 2019-09-29 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vincode',
            name='sekill',
            field=models.ImageField(default=1, upload_to='car_images'),
            preserve_default=False,
        ),
    ]

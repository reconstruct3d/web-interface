# Generated by Django 2.0 on 2018-04-09 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reconstructor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='file_size',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]

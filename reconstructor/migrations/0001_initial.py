# Generated by Django 2.0 on 2018-04-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=60)),
                ('file_name', models.CharField(max_length=60)),
                ('file_format', models.CharField(max_length=10)),
                ('date_created', models.DateField()),
            ],
        ),
    ]
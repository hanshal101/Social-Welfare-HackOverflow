# Generated by Django 4.1.7 on 2023-03-13 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=100)),
            ],
        ),
    ]

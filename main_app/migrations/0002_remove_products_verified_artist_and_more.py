# Generated by Django 4.1.2 on 2022-10-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='verified_artist',
        ),
        migrations.AddField(
            model_name='products',
            name='verified_product',
            field=models.BooleanField(default=False),
        ),
    ]

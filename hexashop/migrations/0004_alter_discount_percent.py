# Generated by Django 3.2.9 on 2021-12-15 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hexashop', '0003_auto_20211215_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='percent',
            field=models.IntegerField(help_text='Enter how much the store wants to sale off.'),
        ),
    ]

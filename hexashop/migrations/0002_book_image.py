# Generated by Django 3.2.9 on 2021-12-14 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hexashop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload the facebook.', null=True, upload_to='uploads/'),
        ),
    ]
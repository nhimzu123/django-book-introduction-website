# Generated by Django 3.2.9 on 2021-12-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hexashop', '0002_book_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title', 'released_date', 'publisher']},
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(),
        ),
    ]
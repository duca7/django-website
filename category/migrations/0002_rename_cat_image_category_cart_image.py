# Generated by Django 3.2.2 on 2021-06-19 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_image',
            new_name='cart_image',
        ),
    ]

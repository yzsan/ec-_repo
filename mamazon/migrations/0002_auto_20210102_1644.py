# Generated by Django 3.1.4 on 2021-01-02 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mamazon', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='description',
        ),
    ]

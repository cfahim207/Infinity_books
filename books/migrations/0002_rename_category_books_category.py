# Generated by Django 5.1.2 on 2024-11-04 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='Category',
            new_name='category',
        ),
    ]
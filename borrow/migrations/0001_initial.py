# Generated by Django 5.1.2 on 2024-10-26 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('readers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowDate', models.DateTimeField(auto_now_add=True)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readers.reader')),
            ],
        ),
    ]

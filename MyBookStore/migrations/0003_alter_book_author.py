# Generated by Django 3.2.9 on 2021-11-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBookStore', '0002_rename_books_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='Write author name here', max_length=25),
        ),
    ]

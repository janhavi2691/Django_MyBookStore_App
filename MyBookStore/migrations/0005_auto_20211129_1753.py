# Generated by Django 3.2.9 on 2021-11-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBookStore', '0004_alter_book_pubyear'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pubyear',
            new_name='Publication Year',
        ),
        migrations.RemoveField(
            model_name='book',
            name='bookid',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=models.PositiveIntegerField(default=0, max_length=13, primary_key=True, serialize=False, unique=True),
        ),
    ]

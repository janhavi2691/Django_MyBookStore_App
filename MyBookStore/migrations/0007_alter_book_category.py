# Generated by Django 3.2.9 on 2021-11-29 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBookStore', '0006_auto_20211129_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('FICT', 'Fiction'), ('NFICT', 'Nonfiction'), ('CL', 'Classic'), ('BI', 'Biography'), ('TECH', 'Technology'), ('OT', 'Other')], max_length=20),
        ),
    ]

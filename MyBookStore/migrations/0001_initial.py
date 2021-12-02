# Generated by Django 3.2.9 on 2021-11-28 18:42

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.lookups


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Enter Author Name', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('title', models.CharField(default='Write book title here', max_length=100)),
                ('language', models.CharField(choices=[('EG', 'English'), ('FR', 'French'), ('GE', 'German'), ('SP', 'Spanish')], max_length=20)),
                ('isbn', models.PositiveIntegerField(default=0)),
                ('pubyear', models.DateField(verbose_name=django.db.models.lookups.YearExact)),
                ('category', models.CharField(choices=[('FICT', 'fiction'), ('NFICT', 'nonfiction'), ('CL', 'classic'), ('BI', 'biography')], max_length=20)),
                ('bookid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBookStore.author')),
            ],
        ),
    ]

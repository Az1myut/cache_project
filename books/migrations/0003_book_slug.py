# Generated by Django 4.1.2 on 2022-11-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='slug'),
        ),
    ]
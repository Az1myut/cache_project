# Generated by Django 4.1.2 on 2022-11-25 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default='Без категории', on_delete=django.db.models.deletion.CASCADE, to='books.genre'),
        ),
    ]

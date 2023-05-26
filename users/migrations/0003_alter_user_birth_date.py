# Generated by Django 4.1.2 on 2022-11-25 18:06

import datetime
from django.db import migrations, models
import users.validators.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_user_avatar_user_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.date(2022, 11, 25), validators=[users.validators.validators.validate_age], verbose_name='Дата рождения'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-07-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0002_alter_bank_fixed_deposit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_website',
            field=models.URLField(max_length=254),
        ),
    ]

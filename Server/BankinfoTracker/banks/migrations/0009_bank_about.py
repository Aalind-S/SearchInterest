# Generated by Django 4.0.1 on 2022-07-14 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0008_remove_bank_saving_acc_fixeddeposit_tenure_savingacc'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='about',
            field=models.TextField(default='text area'),
        ),
    ]

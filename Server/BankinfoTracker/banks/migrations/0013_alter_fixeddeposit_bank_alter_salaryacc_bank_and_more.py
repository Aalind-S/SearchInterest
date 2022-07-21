# Generated by Django 4.0.1 on 2022-07-20 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0012_remove_bank_rural_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixeddeposit',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixeddeposits', to='banks.bank'),
        ),
        migrations.AlterField(
            model_name='salaryacc',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salaryacc', to='banks.bank'),
        ),
        migrations.AlterField(
            model_name='savingacc',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savingacc', to='banks.bank'),
        ),
    ]
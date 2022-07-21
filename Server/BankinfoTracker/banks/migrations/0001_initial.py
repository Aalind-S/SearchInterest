# Generated by Django 4.0.6 on 2022-07-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=180)),
                ('bank_website', models.URLField()),
                ('saving_acc', models.FloatField()),
                ('fixed_deposit', models.FloatField()),
                ('rural_bank', models.FloatField(blank=True, null=True)),
                ('current_acc', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=180)),
                ('Age', models.PositiveSmallIntegerField()),
                ('Salary', models.PositiveIntegerField()),
                ('Email', models.CharField(max_length=254)),
            ],
        ),
    ]

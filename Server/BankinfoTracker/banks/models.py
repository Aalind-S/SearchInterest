from django.db import models


class Bank(models.Model):
    bank_name = models.CharField(max_length=120)
    bank_website = models.URLField()
    saving_acc = models.FloatField()
    fixed_deposit = models.FloatField()
    rural_bank = models.FloatField(blank=True, null=True)
    current_acc = models.FloatField()
    # age
    # salary
    #


class Person(models.Model):
    pass
    Age = models.PositiveSmallIntegerField()
    Salary = models.PositiveIntegerField()

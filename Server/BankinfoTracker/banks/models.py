from django.db import models
from .constants import *


class Bank(models.Model):
    iden = models.CharField(max_length=120, default="identity")
    bank_name = models.CharField(max_length=180)
    bank_website = models.URLField(max_length=254)
    ownership = models.CharField(max_length=40, default="Private")
    #saving_acc = models.FloatField()
    #fixed_deposit = models.FloatField(choices=axis_fd.fd_choices, null=True, blank=True)
    #rural_bank = models.FloatField(blank=True, null=True)
    #current_acc = models.FloatField(blank=True, null=True)
    minimum_balance = models.IntegerField(null=True, blank=True)
    about = models.TextField(default="text area")
    #crisil = models.CharField(max_length=20, default="None")
    #icra = models.CharField(max_length=20, default="None")
    #stock = models.URLField(max_length=254, default="www.example.com")
    # age
    # salary
    #


class Person(models.Model):

    Name = models.CharField(max_length=180)
    Age = models.PositiveSmallIntegerField()
    Salary = models.PositiveIntegerField()
    Email = models.CharField(max_length=254)


class FixedDeposit(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='fixeddeposits')
    tenure = models.CharField(max_length=180, default="around a year")
    regular = models.FloatField()
    senior = models.FloatField()

    def __str__(self):
        return self.tenure + self.str(regular) + self.str(senior)


class SavingAcc(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='savingacc')
    balance = models.CharField(max_length=180, default="10000")
    interest = models.FloatField()


class SalaryAcc(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='salaryacc')
    balance = models.CharField(max_length=180, default="10000")
    interest = models.FloatField()

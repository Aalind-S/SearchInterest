from .models import *
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['bank_name', 'bank_website', 'ownership',
                  'minimum_balance', 'about', 'fixeddeposits', 'salaryacc', 'savingacc']
        depth = 1


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['Name', 'Age', 'Salary', 'Email']


class FixedDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedDeposit
        fields = ['bank', 'tenure', 'regular', 'senior']


class SavingAccSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingAcc
        fields = ['bank', 'balance', 'interest']

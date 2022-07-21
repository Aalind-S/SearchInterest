from django.contrib import admin

from .models import Bank, Person, FixedDeposit, SavingAcc, SalaryAcc


admin.site.register(Bank)
admin.site.register(Person)
admin.site.register(FixedDeposit)
admin.site.register(SavingAcc)
admin.site.register(SalaryAcc)

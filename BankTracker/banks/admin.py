from django.contrib import admin

from .models import Bank

from .models import Person
admin.site.register(Bank)
admin.site.register(Person)

from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Vehicle)
admin.site.register(Book_Vehicle)

# Register your models here.

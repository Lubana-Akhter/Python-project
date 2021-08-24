from django.contrib import admin
from emsapp.models import Department, Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ['department',]
    list_display = ('name','email','dob','gender','salary','department',)

admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)

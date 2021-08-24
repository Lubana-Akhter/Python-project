from django.contrib import admin
from myapp.models import Student, UserProfile


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'dob', 'gender']
    search_fields = ['name', 'email']
    fields = ['name', 'email', 'dob', 'gender']
   # list_editable = ['email', 'dob', 'gender']
    list_per_page = 10
    list_filter = ['gender']
# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(UserProfile)
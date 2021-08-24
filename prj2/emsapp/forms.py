from django import forms
from emsapp.models import Employee, Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

from import_export import resources
from emsapp.models import Employee

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
        exclude = ('photo',)
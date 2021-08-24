from django.shortcuts import render
from emsapp.models import Department, Employee
from emsapp.forms import DepartmentForm, EmployeeForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
class EmployeeListView(ListView):
    template_name = 'employee/list.html'
    model = Employee
    queryset  = Employee.objects.order_by('-id')
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Employee List'
        return context

class EmployeeCreateView(CreateView):
    template_name = 'employee/create.html'
    model = Employee
    form_class = EmployeeForm
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Employee'
        context['heading'] = 'Create new employee'
        return context

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,'Employee save Successfully')
        return reverse("employee:list")

class EmployeeUpdateView(UpdateView):
    template_name = 'employee/create.html'
    model = Employee
    form_class = EmployeeForm
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit employee'
        context['heading'] = 'Update Employee'
        return context

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,'Employee updated Successfully')
        return reverse("employee:list")
    

class EmployeeDeleteView(DeleteView):
    template_name = 'employee/delete.html'
    model = Employee
    form_class = EmployeeForm

    success_url = reverse_lazy('employee:list')

class EmployeeDetailView(DetailView):
    template_name = 'employee/details.html'
    queryset = Employee.objects.all()
    
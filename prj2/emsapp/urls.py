"""
"""
from django.contrib import admin
from django.urls import path
from emsapp import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'emsapp'


urlpatterns = [

    path('list/', views.EmployeeListView.as_view(), name = 'list'),
    path('create/', views.EmployeeCreateView.as_view(), name = 'create'),
    path('edit/<int:pk>', views.EmployeeUpdateView.as_view(), name = 'edit'),
    path('update/<int:pk>', views.EmployeeUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>', views.EmployeeDeleteView.as_view(), name = 'delete'),
    path('details/<int:pk>', views.EmployeeDetailView.as_view(), name = 'details'),
   
]

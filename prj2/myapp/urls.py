"""
"""
from django.contrib import admin
from django.urls import path
from myapp import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'myapp'


urlpatterns = [
   
    path('details/<int:id>', views.show, name = 'details'),
    path('index/', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('edit/<int:id>', views.edit, name = 'edit'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('email/', views.sendEmail, name = 'email'),
    path('register/', views.user_register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('exportdata/', views.exportdata, name = 'export'),
]

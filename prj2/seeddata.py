import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj2.settings')


import django
django.setup()

from myapp.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
#pip install faker
from faker import Faker 
fakegen = Faker() #Faker er object create

def add_student():
    fake_name = fakegen.name()
    fake_email = fakegen.email()
    fake_dob = fakegen.date()

    std = Student.objects.get_or_create(
        name = fake_name,
        email = fake_email,
        dob = fake_dob
    )[0] # list er index number
    return std

def populate_data(n=5):
    for x in range(n):
        std = add_student()


if __name__ == '__main__':
    print("Populating date please wait...")
    print("#" * 80)
    populate_data(21)
    print("populating data complete")
    print("#" * 80)
    try:
        User.objects.get_or_create(
            username = 'sarin',
            password = make_password('sarin'),
            email = 'sarin@love.com',
            first_name = 'Sarin',
            last_name = 'Reza',
            is_staff = True,
            is_superuser = True,
            is_active = True
            )
        print("User Created successfully.")
    except:
        print("User already exists !!!")

    

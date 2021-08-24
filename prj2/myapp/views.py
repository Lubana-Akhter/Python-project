from django.shortcuts import render, redirect
from myapp.models import Student, UserProfile
from myapp.forms import StudentForm, EmailForm,UserForm, UserProfileForm
from django.core.paginator import Paginator
from django.contrib import messages

from django.core.mail import EmailMessage #send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

# for export import
from myapp.resources import EmployeeResource
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'homemap.html', {'title':'Home'})

def index(request):
    std = Student.objects.order_by('-id') 
    paginator = Paginator(std, 20)
    page = request.GET.get('page')
    students =  paginator.get_page(page)
    context = {'title': 'List of students', 'students':students}
    return render(request, 'student/index.html',context)

def show(request,id):
    student = Student.objects.get(pk = id)
    form = StudentForm(request.POST or None, instance = student)
    context = {'title':'Details', 'student':student}
    return render(request, 'student/details.html', context)

def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Student inserted successfully !")
            return redirect('student:index') 
    else:
        form = StudentForm()    
    context = {'title':'Insert', 'form': form}  #this is dictionary
    return render(request, 'student/create.html', context)

def edit(request,id):
    student = Student.objects.get(pk = id)
    form = StudentForm(request.POST or None, instance = student)
    context = {'title':'edit', 'student':student, 'form': form}
    return render(request, 'student/edit.html', context)


def update(request,id):
    student = Student.objects.get(pk = id)
    form = StudentForm(request.POST or None, instance = student)
    if form.is_valid():
        form.save()
        messages.success(request,"Student updated successfully !")
        return redirect('student:index') 
    else:
        print('invalid data')  
    context = {'title':'edit', 'form':form}
    return render(request, 'student/edit.html', context)

def delete(request,id):
    student = Student.objects.get(pk = id)
    student.delete()
    messages.add_message(request, messages.SUCCESS,"Student delete successfully !")
    return redirect('student:index')

def sendEmail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            sub = form.cleaned_data['subject']
            mes = form.cleaned_data['message']
            email = form.cleaned_data['email']
            try:
                mail = EmailMessage(sub, mes, settings.EMAIL_HOST_USER,[email])
                if request.FILES:
                    files = request.FILES.getlist('attach')
                    for f in files:
                        mail.attach(f.name, f.read(), f.content_type)
                    mail.send()
                    messages.success(request, 'Email sent successfully')
                    return redirect('student:index')
            except:
                messages.error(request, 'sorry  !!!  Email not sent !!')
    else:
        form = EmailForm()

    context = {'title':'Email', 'form':form}
    return render(request, 'email_form.html', context) 

# authentication and authorization
def user_register(request):
    if request.method=='POST':
        user_form = UserForm(data = request.POST)
        user_profile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = user_profile_form.save(commit = False)
            user_profile.user = user

            if 'profile_pic' in request.FILES:
                user_profile.profile_pic = request.FILES['profile_pic']


            user_profile.save()
            messages.success(request, 'You have been registered successfully')
            return redirect('student:index')
        
    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm(data = request.POST)
    context = {'user_form':user_form, 'user_profile_form':user_profile_form}
    return render (request,'auth/register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            login(request, user)
            # get profile info
            profile = UserProfile.objects.get(user=request.user)
            if profile:
                request.session['profile_pic'] = profile.profile_pic.url
                request.session['profile_type'] = profile.user_type
            # end of get profile info
            
            return redirect('student:index')
        else:
            messages.error(request,'Error login ..try again later')
            return redirect('student:login')
    else:
        return render(request,'auth/login.html',{})

def user_logout(request):
    logout(request)
    messages.success(request,'You have been loggedout')
    return redirect('student:index')

def exportdata(request):
    if request.method == 'POST':
        file_format = request.POST['file_format']
        employee_resource = EmployeeResource()
        dataset = employee_resource.export()

        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type = 'text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response

        if file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type = 'application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response

        if file_format == 'XLS':
            response = HttpResponse(dataset.xls, content_type = 'application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response

        if file_format == 'HTML':
            response = HttpResponse(dataset.html, content_type = 'text/html')
            response['Content-Disposition'] = 'attachment; filename="exported_data.html"'
            return response

    return render(request, 'export.html')
from django.shortcuts import render,redirect
#from EskoolyApp.forms import studentForm,studentAddForm,teacherForm,teacherAddForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from EskoolyApp.models import Classes, Subjects
from django.contrib.auth.models import User
# from EskoolyApp.forms import AdminLogin,StudentLogin,TeacherLogin
from .decorators import unauthenticated_user, allowed_users,admin_only
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, View, DeleteView, UpdateView, TemplateView
from django.utils.decorators import method_decorator

# Create your views here.
decoratorss = [login_required, admin_only]
def index(request):
    return render(request,'EskoolyApp/index.html')

@login_required(login_url='login')
@admin_only
def adminhome(request):
    return render(request, 'EskoolyApp/adminhome.html')

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminhome')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'EskoolyApp/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
def studentDash(request):
    return render(request, 'EskoolyApp/studentDash.html', {})

def teacherDash(request):
    return render(request, 'EskoolyApp/teacherDash.html', {})

@login_required(login_url='login')
@admin_only
def dashboard(request):
    return render(request, 'EskoolyApp/dashboard.html', {})

@method_decorator(decoratorss, name='dispatch')
class ClassesCreateView(CreateView):
    model = Classes
    fields = '__all__'
    def get_success_url(self):
        return reverse('index')

@method_decorator(decoratorss, name='dispatch')
class ClassesListView(ListView):
    model = Classes

@method_decorator(decoratorss, name='dispatch')
class ClassesDetailView(DetailView):
    model = Classes
@method_decorator(decoratorss, name='dispatch')
class ClassesUpdateView(UpdateView):
    model = Classes
    fields = '__all__'
    def get_success_url(self):
        return reverse('index')
@method_decorator(decoratorss, name='dispatch')
class ClassesDeleteView(DeleteView):
    model = Classes
    def get_success_url(self):
        return reverse('listclass')

@login_required(login_url='login')
@admin_only
def SubjectsView(request):
    return render(request, 'EskoolyApp/viewsubjects.html', {'classes': Classes.objects.all()})

@method_decorator(decoratorss, name='dispatch')
class SubjectsAddView(CreateView):
    model = Subjects
    fields = '__all__'
    def get_success_url(self):
        return reverse('index')

@method_decorator(decoratorss, name='dispatch')
class SubjectsUpdateView(UpdateView):
    model = Subjects
    fields = '__all__'
    def get_success_url(self):
        return reverse('index')


# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("Your account was inactive.")
#         else:
#             print("Someone tried to login and failed.")
#             print("They used username: {} and password: {}".format(username,password))
#             return HttpResponse("Invalid login details given")
#     else:
#         return render(request, 'EskoolyApp/login.html', {})
# @login_required
# def userLogout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))
#
#
# def register(request):
#     return render(request,'EskoolyApp/register.html')
#
# def registerStudent(request):
#     registered=False
#     if request.method=='POST':
#         var_studentForm=studentForm(request.POST)
#         var_studentAddForm=studentAddForm(request.POST)
#         if var_studentForm.is_valid() and var_studentAddForm.is_valid():
#             studentprimary=var_studentForm.save()
#             studentprimary.set_password(studentprimary.password)
#             studentprimary.save()
#             studentAdd=var_studentAddForm.save(commit=False)
#             studentAdd.student=studentprimary
#             studentAdd.save()
#             registered=True
#     else:
#         var_studentForm=studentForm()
#         var_studentAddForm=studentAddForm()
#     return render(request,'EskoolyApp/registerStudent.html',{'var_studentForm':var_studentForm,'var_studentAddForm':var_studentAddForm,'registered':registered})
#
#
# def registerTeacher(request):
#     registered=False
#     if request.method=='POST':
#         var_teacherForm=teacherForm(request.POST)
#         var_teacherAddForm=teacherAddForm(request.POST)
#         if var_teacherForm.is_valid() and var_teacherAddForm.is_valid():
#             teacherprimary=var_teacherForm.save()
#             teacherprimary.set_password(teacherprimary.password)
#             teacherprimary.save()
#             teacherAdd=var_teacherAddForm.save(commit=False)
#             teacherAdd.teacher=teacherprimary
#             teacherAdd.save()
#             registered=True
#     else:
#         var_teacherForm=teacherForm()
#         var_teacherAddForm=teacherAddForm()
#     return render(request,'EskoolyApp/registerTeacher.html',{'var_teacherForm':var_teacherForm,'var_teacherAddForm':var_teacherAddForm,'registered':registered})
#
# def userLogin(request):
#     invalidlogin=False
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(username=username,password=password)
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse('Account not active')
#         else:
#             invalidlogin=True
#             return redirect('/EskoolyApp/login/')
#     else:
#         return render(request,'EskoolyApp/login.html',{'invalidlogin':invalidlogin})
#
# @login_required
# def dashboard(request):
#     try:
#         current=Student.objects.get(student=request.user)
#     except Student.DoesNotExist:
#         current=Teacher.objects.get(teacher=request.user)
#     if current.is_student:
#         return redirect('/studentDash/')
#     else:
#         return redirect('/teacherDash/')
#     return render(request,'EskoolyApp/dashboard.html')
#
#
#
# def studentDash(request):
#     return render(request,'EskoolyApp/studentDash.html')
#
# def teacherDash(request):
#     return render(request,'EskoolyApp/teacherDash.html')

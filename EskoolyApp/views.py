from django.shortcuts import render,redirect, get_object_or_404
#from EskoolyApp.forms import studentForm,studentAddForm,teacherForm,teacherAddForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from EskoolyApp.models import Classes, Subjects, InstituteInfo, Students
from django.contrib.auth.models import User
from EskoolyApp.forms import InstituteInfoForm, RulesForm, FeesForm
from .decorators import unauthenticated_user, allowed_users,admin_only
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, View, DeleteView, UpdateView, TemplateView
from django.utils.decorators import method_decorator
from django.db.models import Q
# Create your views here.
decoratorss = [login_required(login_url='login'), admin_only]
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

def view_institute_info(request, id):
    obj= get_object_or_404(InstituteInfo, id=id)
    obj1= get_object_or_404(InstituteInfo, id=id)
    obj2= get_object_or_404(InstituteInfo, id=id)
    inst_info = InstituteInfo.objects.all()
    institute_info_form = InstituteInfoForm()
    rules_form = RulesForm()
    fees_form = FeesForm()
    mydict = {'institute_info_form': institute_info_form, 'inst_info': inst_info, 'rules_form':rules_form, 'fees_form':fees_form}
    if request.method == 'POST':
        institute_info_form = InstituteInfoForm(request.POST,request.FILES, instance = obj)
        rules_form = RulesForm(request.POST, instance = obj1)
        fees_form = FeesForm(request.POST, instance = obj2)
        if institute_info_form.is_valid():
            obj = institute_info_form.save()
            obj.save()
            mydict = {'institute_info_form': institute_info_form, 'inst_info': inst_info,'rules_form':rules_form, 'fees_form':fees_form}
        if rules_form.is_valid():
            obj1 = rules_form.save()
            obj1.save()
            mydict = {'institute_info_form': institute_info_form, 'inst_info': inst_info,'rules_form':rules_form, 'fees_form':fees_form}
        if fees_form.is_valid():
            obj2 = fees_form.save()
            obj2.save()
            mydict = {'institute_info_form': institute_info_form, 'inst_info': inst_info,'rules_form':rules_form, 'fees_form':fees_form}

    return render(request,'EskoolyApp/viewinstituteinfo.html', context = mydict)

@method_decorator(decoratorss, name='dispatch')
class StudentsAddView(CreateView):
    model = Students
    fields = '__all__'
    def get_success_url(self):
        return reverse('index')

@login_required(login_url='login')
@admin_only
def StudentsView(request):
    return render(request, 'EskoolyApp/viewstudents.html', {'students': Students.objects.all()})


@method_decorator(decoratorss, name='dispatch')
class StudentsDetailView(DetailView):
    model = Students

@method_decorator(decoratorss, name='dispatch')
class StudentsUpdateView(UpdateView):
    model = Students
    fields = '__all__'
    def get_success_url(self):
        return reverse('index')

@method_decorator(decoratorss, name='dispatch')
class StudentsDeleteView(DeleteView):
    model = Students
    def get_success_url(self):
        return reverse('view_students')

@login_required(login_url='login')
@admin_only
def StudentAdmissionLetter(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(reg_no__icontains=query) | Q(name__icontains=query)

            results= Students.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'EskoolyApp/admission_letter.html', context)

        else:
            return render(request, 'EskoolyApp/admission_letter.html')

    else:
        return render(request, 'EskoolyApp/admission_letter.html')

@login_required(login_url='login')
@admin_only
def PrintAdmissionLetter(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(reg_no__icontains=query) | Q(name__icontains=query)

            results= Students.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'EskoolyApp/print_admission_letter.html', context)

        else:
            return render(request, 'EskoolyApp/print_admission_letter.html')

    else:
        return render(request, 'EskoolyApp/print_admission_letter.html')

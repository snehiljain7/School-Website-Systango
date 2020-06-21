"""EskoolyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from EskoolyApp import views
from django.conf.urls.static import static
from django.conf import settings

#app_name=''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    # path('accounts/',include('django.contrib.auth.urls')),
    path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    path('studentDash/',views.studentDash, name="studentDash"),
    path('dashboard/',views.dashboard, name = "dashboard"),
    path('teacherDash/',views.teacherDash, name="teacherDash"),
    path('adminhome/',views.adminhome, name="adminhome"),
    path('create/', views.ClassesCreateView.as_view()),
    path('listclass/',views.ClassesListView.as_view(), name = 'listclass'),
    path('detail/<pk>',views.ClassesDetailView.as_view()),
    path('update/<pk>', views.ClassesUpdateView.as_view()),
    path('delete/<pk>', views.ClassesDeleteView.as_view()),
    path('viewsubjects/', views.SubjectsView),
    path('addsubjects/', views.SubjectsAddView.as_view()),
    path('updatesubject/<pk>', views.SubjectsUpdateView.as_view()),
    path('instituteinfo/<id>', views.view_institute_info),
    path('addstudent/', views.StudentsAddView.as_view()),
    path('viewstudents/', views.StudentsView, name = 'view_students'),
    path('studentsdetail/<pk>',views.StudentsDetailView.as_view()),
    path('updatestudents/<pk>',views.StudentsUpdateView.as_view()),
    path('deletestudents/<pk>', views.StudentsDeleteView.as_view()),
    path('admissionletter/', views.StudentAdmissionLetter),
    path('printadmissionletter/', views.PrintAdmissionLetter),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

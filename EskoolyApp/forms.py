from django import forms
from django.contrib.auth.models import User
from EskoolyApp.models import InstituteInfo

LOCATIONS = (
    ('IND', 'India'),
    ('PAK', 'Pakistan'),
    ('ENG', 'England'),
    ('AUS', 'Australia'),
    ('SA', 'South Africa'),
)
class InstituteInfoForm(forms.ModelForm):
    location = forms.ChoiceField(choices=LOCATIONS, required=True)
    class Meta:
        model = InstituteInfo
        fields = ['id','institute_name', 'target_line', 'logo', 'phone', 'website', 'address', 'location']
        widgets = {
            'institute_name': forms.TextInput(attrs={'placeholder': 'Institue name'}),
            'target_line': forms.TextInput(attrs={'placeholder': 'Taget Line'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'website': forms.TextInput(attrs={'placeholder': 'Website'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
        }

class RulesForm(forms.ModelForm):
    rules = forms.CharField(widget = forms.Textarea(attrs={'width':"70%", 'cols': "30" , 'rows':"20"}))
    class Meta:
        model = InstituteInfo
        fields = ['rules']

class FeesForm(forms.ModelForm):
    class Meta:
        model = InstituteInfo
        fields = ['addfee', 'regfee', 'artfee', 'transportfee', 'booksfee', 'uniformfee', 'fine', 'others']
        widgets = {
            'addfee': forms.TextInput(attrs={'placeholder': 'ADMISSION FEE'}),
            'regfee': forms.TextInput(attrs={'placeholder': 'REGISTRATION FEE'}),
            'artfee': forms.TextInput(attrs={'placeholder': 'ART MATERIAL'}),
            'transportfee': forms.TextInput(attrs={'placeholder': 'TRANSPORT FEE'}),
            'booksfee': forms.TextInput(attrs={'placeholder': 'BOOKS FEE'}),
            'uniformfee': forms.TextInput(attrs={'placeholder': 'UNIFORM FEE'}),
            'fine': forms.TextInput(attrs={'placeholder': 'FINE'}),
            'others': forms.TextInput(attrs={'placeholder': 'OTHERS'}),
        }

# class AdminLogin(forms.ModelForm):
#     password=forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = '__all__'
#
# class TeacherLogin(forms.ModelForm):
#     password=forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = Teacher
#         fields = '__all__'

# class studentForm(forms.ModelForm):
#     password=forms.CharField(widget=forms.PasswordInput())
#     class Meta():
#         model=User
#         fields=['first_name','last_name','username','email','password']
#
# BRANCH_CHOICES = (
#     ('COMPS','COMPS'),
#     ('IT','IT'),
#     ('EXTC','EXTC')
# )
# class studentAddForm(forms.ModelForm):
#     branch=forms.CharField(widget=forms.Select(choices=BRANCH_CHOICES))
#     class Meta():
#         model=Student
#         fields=['idno','branch']
#
# class teacherForm(forms.ModelForm):
#     password=forms.CharField(widget=forms.PasswordInput())
#     class Meta():
#         model=User
#         fields=['first_name','last_name','username','email','password']
#
# SUBJECT_CHOICES=(
#     ('DS','Data Structures'),
#     ('DLD','Digital Logic Design'),
#     ('DM','Discrete Mathematics'),
#     ('LA','Linear Algebra')
# )
#
# class teacherAddForm(forms.ModelForm):
#     subject=forms.CharField(widget=forms.Select(choices=SUBJECT_CHOICES))
#     class Meta():
#         model=Teacher
#         fields=['subject','phone']

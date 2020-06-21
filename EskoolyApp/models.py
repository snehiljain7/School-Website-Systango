from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Classes(models.Model):
    name = models.CharField(max_length = 40)
    monthly_fees = models.IntegerField()
    def __str__(self):
        return self.name

class Subjects(models.Model):
    sub_name = models.CharField(max_length = 40)
    weightage = models.IntegerField()
    class_name = models.ForeignKey(Classes, on_delete=models.CASCADE, default="")
    def __str__(self):
        return self.class_name

LOCATIONS = (
    ('IND', 'India'),
    ('PAK', 'Pakistan'),
    ('ENG', 'England'),
    ('AUS', 'Australia'),
    ('SA', 'South Africa'),
)
GENDER_CHOICES = (
                    ('male','Male'),
                    ('female','Female'),
                    ('other','Other')
                    )
RELIGION_CHOICES = (
                    ('buddhism','Buddhism'),
                    ('christianity','Christianity'),
                    ('hinduism','Hinduism'),
                    ('islam','Islam'),
                    ('jainism','Jainism'),
                    ('sikhism','Sikhism'),
                    ('other','Other')
                )

class InstituteInfo(models.Model):
    institute_name = models.CharField(max_length = 40)
    target_line = models.CharField(max_length = 100)
    logo = models.FileField(upload_to = 'images/')
    phone = models.IntegerField()
    website = models.URLField(max_length = 200)
    address = models.CharField(max_length = 80)
    location = models.CharField(max_length=3, choices=LOCATIONS)
    rules = models.CharField(max_length=1000, default = "aaabbbbsbsbsb")
    addfee = models.CharField(max_length = 40, default="")
    regfee = models.CharField(max_length = 40, default="")
    artfee = models.CharField(max_length = 40, default="")
    transportfee = models.CharField(max_length = 40, default="")
    booksfee = models.CharField(max_length = 40, default="")
    uniformfee = models.CharField(max_length = 40, default="")
    fine = models.CharField(max_length = 40, default="")
    others = models.CharField(max_length = 40, default="")

class Students(models.Model):
    name = models.CharField(max_length = 30)
    reg_no = models.IntegerField()
    name_of_class = models.ForeignKey(Classes,on_delete = models.CASCADE)
    picture = models.FileField(upload_to = "images/", null=True, blank=True)
    admission_date = models.DateField()
    discount = models.IntegerField()
    mobile_no = models.IntegerField()
    birthdate = models.DateField(null=True, blank=True)
    orphan_student = models.BooleanField(null=True, blank=True)
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES, null=True, blank=True)
    caste = models.CharField(max_length = 30, null=True, blank=True)
    previous_school = models.CharField(max_length = 50, null=True, blank=True)
    religion = models.CharField(max_length = 20,choices = RELIGION_CHOICES,null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    total_children = models.IntegerField(null=True, blank=True)
    father_name = models.CharField(max_length = 20,null=True, blank=True)
    father_education = models.CharField(max_length = 20,null=True, blank=True)
    father_occupation = models.CharField(max_length = 20,null=True, blank=True)
    father_income = models.FloatField(null=True, blank=True)
    father_mobile = models.IntegerField(null=True, blank=True)
    mother_name = models.CharField(max_length = 20, null=True, blank=True)
    mother_education = models.CharField(max_length = 20,null=True, blank=True)
    mother_occupation = models.CharField(max_length = 20,null=True, blank=True)
    mother_income = models.FloatField(null=True, blank=True)
    mother_mobile = models.IntegerField(null=True, blank=True)

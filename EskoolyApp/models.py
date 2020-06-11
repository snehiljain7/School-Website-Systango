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

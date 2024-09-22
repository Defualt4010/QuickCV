from django.db import models

'''
    A Person can have attended more than 1 college thus the mail Resume Class will have many College Objects.
'''
# class CollegeDetails(models.Model):
#     college_name = models.CharField(max_length=512)
#     college_start_year = models.DateField()
#     college_end_year = models.DateField()
#     college_activity = models.CharField(max_length=1024)
#     college_pointers = models.FloatField()

# Create your models here.
class Resume(models.Model):
    # Personal Details
    first_name = models.CharField(max_length=256, null=False)
    last_name = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=256)
    phone = models.BigIntegerField()
    about = models.CharField(max_length=2048)

    # College Details 
    college_name = models.CharField(max_length=512)
    college_start_year = models.DateField()
    college_end_year = models.DateField()
    college_activity = models.CharField(max_length=1024)
    college_pointers = models.FloatField()

    

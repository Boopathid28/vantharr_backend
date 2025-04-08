from django.db import models
from courses.models import *

# Create your models here.

class StudentRegistrationDetails(models.Model):

    student_name = models.CharField(max_length=150,verbose_name="Student Name")
    mobile = models.CharField(max_length=150,verbose_name="Mobile Number")
    email = models.EmailField(verbose_name="Email",null=True,blank=True)
    state = models.CharField(max_length=150,verbose_name="State")
    course_details = models.ForeignKey(CourseDetails,verbose_name="Course Details",on_delete=models.PROTECT,null=True,blank=True)
    city = models.CharField(max_length=150,verbose_name="City")
    remark = models.TextField(verbose_name="Remark",null=True,blank=True)
    create_at = models.DateTimeField(verbose_name="Create at")

    class Meta:
        db_table = 'student_details'
        verbose_name = 'student_details'
        verbose_name_plural = 'student_details'

    def __str__(self):
        return self.student_name

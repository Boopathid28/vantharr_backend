from rest_framework import serializers
from .models import *

class CourseCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCategory
        fields = '__all__'
        

class CourseDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseDetails
        fields = '__all__'
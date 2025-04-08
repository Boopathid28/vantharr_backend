from rest_framework import serializers
from .models import *

class StudentRegistrationDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentRegistrationDetails
        fields = '__all__'
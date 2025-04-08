from rest_framework import serializers
from .models import *

class BlogDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogDetails
        fields = '__all__'
        
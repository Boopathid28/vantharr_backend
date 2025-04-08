from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.views import APIView
from django.utils import timezone
from django.core.paginator import Paginator
from django.conf import settings

from .models import *
from.serializer import *

class StudentRegistrationView(APIView):

    def post(self,request):

        request_data = request.data

        request_data['create_at'] = timezone.now()

        serializer = StudentRegistrationDetailsSerializer(data=request_data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "data":serializer.data,
                    "message":"Student Registered Sucessfully",
                    "status":status.HTTP_200_OK
                },status=status.HTTP_200_OK
            )
        
        else:

            return Response(
                {
                    "data":serializer.errors,
                    "message":"Student Not Registered",
                    "status":status.HTTP_400_BAD_REQUEST
                },status=status.HTTP_200_OK
            )


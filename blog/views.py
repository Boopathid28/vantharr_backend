from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.views import APIView
from django.utils import timezone
from django.core.paginator import Paginator
from django.conf import settings

from .models import *
from .serializer import *

class BlogDetailsView(APIView):

    def get(self,request):

        try:

            pk = request.GET.get('id',None)

            if pk == None:

                return Response(
                    {
                        "message":"Please Enter the ID",
                        "status":status.HTTP_204_NO_CONTENT
                    },status=status.HTTP_200_OK
                )
            
            queryset = BlogDetails.objects.get(id=pk)

            serializer = BlogDetailsSerializer(queryset)

            res_data = serializer.data

            res_data['blog_image'] = settings.IMAGE_URL+str(queryset.blog_image)

            return Response(
                {
                    "data":res_data,
                    "message":"Blog Retrieved Sucessfully",
                    "stauts":status.HTTP_200_OK
                },status=status.HTTP_200_OK
            )
        
        except BlogDetails.DoesNotExist:

            return Response(
                {
                    "message":"Blog Doesnot Exsist",
                    "status":status.HTTP_404_NOT_FOUND
                },status=status.HTTP_200_OK
            )

        except Exception as err:

            return Response(
                {
                    "data":str(err),
                    "status":status.HTTP_204_NO_CONTENT
                },status=status.HTTP_200_OK
            )
        
class BlogDetailsListView(APIView):

    def post(self,request):

        search = request.data.get('search',"")
        page = request.data.get('page',1)
        items_per_page = request.data.get('items_per_page',10)


        filter_condition = {}

        if search != None:

            filter_condition['blog_title__icontains'] = search


        filter_condition['is_active'] = True

        queryset = BlogDetails.objects.filter(**filter_condition).order_by('-id')

        paginated_data = Paginator(queryset, items_per_page)
        serializer = BlogDetailsSerializer(paginated_data.get_page(page), many=True)
        total_items = len(queryset)

        response_data = []

        for data in serializer.data:

            blog_queryset = BlogDetails.objects.get(id=data['id'])

            res_data = data

            res_data['blog_image'] = settings.IMAGE_URL+str(blog_queryset.blog_image)

            response_data.append(res_data)

        return Response(
            {
                "data":{
                    "list":response_data,
                    "total_pages": paginated_data.num_pages,
                    "current_page": page,
                    "total_items": total_items,
                    "current_items": len(serializer.data)
                },
                "message":"Blog Table List",
                "status":status.HTTP_200_OK
            },status=status.HTTP_200_OK
        )
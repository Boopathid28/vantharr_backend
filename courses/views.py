from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.views import APIView
from django.utils import timezone
from django.core.paginator import Paginator
from django.conf import settings

from courses.models import CourseCategory, CourseDetails
from courses.serializer import CourseDetailsSerializer


class CategoryListView(APIView):

    def get(self,request):

        queryset = CourseCategory.objects.all().order_by('-id').values('id','category_name')

        return Response(
            {
                "data":queryset,
                "message":"Category Dropdown List",
                "status":status.HTTP_200_OK
            },status=status.HTTP_200_OK
        )

class CourseDetailsView(APIView):

    def get(self,request):

        try:

            pk = request.GET.get('id',None)

            if pk == None:

                return Response(
                    {
                        "message":"Please Enter the ID",
                        "stauts":status.HTTP_204_NO_CONTENT
                    },status=status.HTTP_200_OK
                )
            
            queryset = CourseDetails.objects.get(course_url=pk)

            serializer = CourseDetailsSerializer(queryset)

            res_data = serializer.data

            res_data['category_name'] = queryset.category.category_name
            res_data['course_image'] = settings.IMAGE_URL+str(queryset.course_image)

            return Response(
                {
                    "data":res_data,
                    "message":"Course Retrieved Sucessfully",
                    "status":status.HTTP_200_OK
                },status=status.HTTP_200_OK
            )
        
        except CourseDetails.DoesNotExist:
            print("hi")

            return Response(
                {
                    "message":"Course Doesnot Exsist",
                    "status":status.HTTP_404_NOT_FOUND
                },status=status.HTTP_200_OK
            )

        except Exception as err:

            return Response(
                {
                    "data":str(err),
                    "message":"Something Went Wrong",
                    "status":status.HTTP_204_NO_CONTENT
                },status=status.HTTP_200_OK
            )
        

class CourseDetailsListView(APIView):

    def get(self, request):

        queryset = list(CourseDetails.objects.filter(is_active=True).order_by('-id').values('id', 'course_title'))


        return Response(
            {
                "data":{
                    "list":queryset
                },
                "message":"Course List",
                "status":status.HTTP_200_OK
            },status=status.HTTP_200_OK
        )

    def post(self,request):


        search = request.data.get('search',"")
        category = request.data.get('category',None)
        page = request.data.get('page',1)
        items_per_page = request.data.get('items_per_page',10)


        filter_condition = {}

        if search != None:

            filter_condition['course_title__icontains'] = search

        if category != None:

            filter_condition['category'] = category

        filter_condition['is_active'] = True

        queryset = CourseDetails.objects.filter(**filter_condition).order_by('-id')

        paginated_data = Paginator(queryset, items_per_page)
        serializer =CourseDetailsSerializer(paginated_data.get_page(page), many=True)
        total_items = len(queryset)

        response_data = []

        for data in serializer.data:

            course_queryset = CourseDetails.objects.get(id=data['id'])

            res_data = data

            res_data['category_name'] = course_queryset.category.category_name
            res_data['course_image'] = settings.IMAGE_URL+str(course_queryset.course_image)

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
                "message":"Course Table List",
                "status":status.HTTP_200_OK
            },status=status.HTTP_200_OK
        )

        
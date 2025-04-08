from django.urls import path

from courses.views import CategoryListView, CourseDetailsListView, CourseDetailsView

urlpatterns = [
   path('course-details/',CourseDetailsView.as_view()),
   path('course-details-list/',CourseDetailsListView.as_view()),
   path('category-list/',CategoryListView.as_view()),
]
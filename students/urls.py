from django.urls import path

from students.views import StudentRegistrationView


urlpatterns = [
    path('student-registration/',StudentRegistrationView.as_view()),
]
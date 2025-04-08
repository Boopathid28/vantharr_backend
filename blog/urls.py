from django.urls import path

from blog.views import BlogDetailsListView, BlogDetailsView


urlpatterns = [
    path('blog-details/',BlogDetailsView.as_view()),
    path('blog-details-list/',BlogDetailsListView.as_view()),
]
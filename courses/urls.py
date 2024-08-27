from django.urls import path
from .views import CourseListCreate, InstanceListCreate

urlpatterns = [
    # URL for listing and adding courses
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),

    # URL for listing and adding instances
    path('instances/', InstanceListCreate.as_view(), name='instance-list-create'),
]

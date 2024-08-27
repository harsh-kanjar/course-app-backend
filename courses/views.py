from django.shortcuts import render
from rest_framework import generics
from .models import Course, Instance
from .serializers import CourseSerializer, InstanceSerializer

# Course Views
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Instance Views
class InstanceListCreate(generics.ListCreateAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

class InstanceDetail(generics.RetrieveDestroyAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return Instance.objects.filter(year=year, semester=semester)

class InstanceDetailByCourse(generics.RetrieveDestroyAPIView):
    serializer_class = InstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['course_id']
        return Instance.objects.filter(year=year, semester=semester, course_id=course_id)


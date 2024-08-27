from django.urls import path
from .views import CourseListCreate, CourseDetail, InstanceListCreate, InstanceDetail, InstanceDetailByCourse
from courses import views

urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('instances/', InstanceListCreate.as_view(), name='instance-list'),
    path('instances/<int:year>/<int:semester>/', InstanceDetail.as_view(), name='instance-detail'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', InstanceDetailByCourse.as_view(), name='instance-detail-by-course'),
    path('api/instances/', views.InstanceListCreateView.as_view(), name='instance-list-create'),
    path('api/instances/<int:pk>/', views.InstanceDetailView.as_view(), name='instance-detail'),
]

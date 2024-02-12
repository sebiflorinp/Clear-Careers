from django.urls import path, include
from .views import RetrieveUpdateDeleteEmployees, CreateListEmployees

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('employees/<int:employee_id>', RetrieveUpdateDeleteEmployees.as_view(), name='retrieve-update-delete-employees'),
    path('employees/', CreateListEmployees.as_view(), name='create-list-employees')
]
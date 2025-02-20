from django.urls import path
from .views import PropertyCreateAPIView, AllPropertyAPIView

urlpatterns = [
    path('create-property/', PropertyCreateAPIView.as_view(), name='create-property'),
    path('all-properties/', AllPropertyAPIView.as_view(), name="all-properties"),
    path('property/<int:id>/', AllPropertyAPIView.as_view(), name='specific-property'),


]

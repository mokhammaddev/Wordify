from django.urls import path
from .views import ContactRUDAPIView, ContactListCreateAPIView


urlpatterns = [
    path('list-create/', ContactListCreateAPIView.as_view()),
    path('rud/<int:pk>/', ContactRUDAPIView.as_view()),
]
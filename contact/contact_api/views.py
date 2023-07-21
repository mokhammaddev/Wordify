from rest_framework import generics
from .serializers import ContactSerializer
from ..models import Contact


class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

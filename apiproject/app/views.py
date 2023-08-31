from django.shortcuts import get_object_or_404
from app.serializers import ContactSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from app.models import Contact
from rest_framework import status


class ContactViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Contact.objects.all()
        contact = get_object_or_404(queryset, pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def create(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

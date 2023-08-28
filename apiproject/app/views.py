from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from app.models import Contact
from app.serializers import ContactSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


###Writing regular Django views using our Serializer
# @csrf_exempt
# def api_list(request):
#     if request.method == "GET":
#         apivar = Contact.objects.all()
#         serializer = ContactSerializer(apivar, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ContactSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def api_detail(request, pk):
#     try:
#         dvar = Contact.objects.get(pk=pk)
#     except Contact.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = ContactSerializer(dvar)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ContactSerializer(dvar, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         dvar.delete()
#         return HttpResponse(status=204)


###Pulling it all together


@api_view(["GET", "POST"])
def api_list(request):
    if request.method == "GET":
        snip = Contact.objects.all()
        serializer = ContactSerializer(snip, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def api_detail(request, pk):
    try:
        snip = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ContactSerializer(snip)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ContactSerializer(snip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

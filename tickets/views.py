from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tickets.models import *
from tickets.serializers import *

# Create your views here.


# 1. Without RESTful and Without Model FBV
def FBV_WithoutRESTfulAndWithoutModel(request):
    guests = [
        {
            "id": 1,
            "first_name": "Abdullah",
            "middle_name": "Kamal",
            "last_name": "Abdel-Sadek",
            "phone": "01234567890",
            "date_of_birth": "2023-11-20",
        },
        {
            "id": 2,
            "first_name": "Abdullah 2",
            "middle_name": "Kamal 2",
            "last_name": "Abdel-Sadek 2",
            "phone": "01234567891",
            "date_of_birth": "2023-11-20",
        },
    ]
    return JsonResponse(data=guests, safe=False)


# 2. Without RESTful and With Model FBV
def FBV_WithoutRESTfulAndWithModel(request):
    guests = Guest.objects.all()
    response = {
        "guests": list(guests.values()),
    }
    return JsonResponse(data=response)


# 3. With RESTful and With Model List Guests FBV
@api_view(["GET"])
def FBV_WithRESTfulAndWithModelListGuests(request):
    guests = Guest.objects.all()
    serializer = GuestSerializer(guests, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 4. With RESTful and With Model Create Guest FBV
@api_view(["POST"])
def FBV_WithRESTfulAndWithModelCreateGuest(request):
    serializer = GuestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

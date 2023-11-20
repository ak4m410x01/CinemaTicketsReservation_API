from django.shortcuts import render
from django.http.response import JsonResponse
from tickets.models import *

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

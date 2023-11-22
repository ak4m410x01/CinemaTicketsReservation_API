from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from tickets.models import *
from tickets.serializers import *

# Create your views here.


# 1. FBV Without Model and Without RESTful
def fbv_withoutModel_withoutRESTful(request):
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


# 2. FBV With Model and Without RESTful
def fbv_withModel_withoutRESTful(request):
    guests = Guest.objects.all()
    response = {
        "guests": list(guests.values()),
    }
    return JsonResponse(data=response)


# 3. FBV With Model and With RESTful List Guests
@api_view(["GET"])
def fbv_withModel_withRESTful_listGuests(request):
    guests = Guest.objects.all()
    serializer = GuestSerializer(guests, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 4. FBV With Model and With RESTful List Guest
@api_view(["GET"])
def fbv_withModel_withRESTful_listGuest(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GuestSerializer(guest)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 5. FBV With Model and With RESTful Create Guest
@api_view(["POST"])
def fbv_withModel_withRESTful_createGuest(request):
    serializer = GuestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# 6. FBV With Model and With RESTful Update Guest
@api_view(["PUT"])
def fbv_withModel_withRESTful_updateGuest(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GuestSerializer(guest, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


# 7. FBV With Model and With RESTful Delete Guest
@api_view(["DELETE"])
def fbv_withModel_withRESTful_deleteGuest(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    guest.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# 8. CBV With Model and With RESTful List And Create Guest
class CBVWithModelWithRESTfulListAndCreateGuest(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# 9. CBV With Model and With RESTful Get And Update And Delete Guest
class CBVWithModelWithRESTfulGetAndUpdateAndDeleteGuest(APIView):
    def get(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GuestSerializer(guest)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            guest = Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 10. Mixins With Model and With RESTful List And Create Guest
class MixinsWithModelWithRESTfulListAndCreateGuest(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# 11. Mixins With Model and With RESTful Get And Update And Delete Guest
class MixinsWithModelWithRESTfulGetAndUpdateAndDeleteGuest(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)

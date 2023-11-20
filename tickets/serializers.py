from rest_framework import serializers
from tickets.models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = [
            "pk",
            "first_name",
            "middle_name",
            "last_name",
            "phone",
            "date_of_birth",
            "reservations",
        ]


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

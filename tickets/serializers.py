from rest_framework import serializers
from tickets.models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Guest
        fields = [
            "pk",
            "full_name",
            "phone",
            "date_of_birth",
            "reservations",
        ]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.middle_name} {obj.last_name}"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "body",
            "author",
        ]

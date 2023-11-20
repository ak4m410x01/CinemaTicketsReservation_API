from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=30)
    hall = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class Guest(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class Reservation(models.Model):
    movie = models.ForeignKey(Movie, models.CASCADE, related_name="reservations")
    guest = models.ForeignKey(Guest, models.CASCADE, related_name="reservations")
    reserved_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.movie}:{self.guest}"

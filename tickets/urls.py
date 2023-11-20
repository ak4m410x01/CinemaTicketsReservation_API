from django.urls import path
from tickets import views

app_name = "tickets"

urlpatterns = [
    # 1. Without RESTful and Without Model FBV
    path(
        "FBV_WithoutRESTfullAndWithoutModel/",
        views.FBV_WithoutRESTfullAndWithoutModel,
        name="FBV_WithoutRESTfullAndWithoutModel",
    )
]

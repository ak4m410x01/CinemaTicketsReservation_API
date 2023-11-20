from django.urls import path
from tickets import views

app_name = "tickets"

urlpatterns = [
    # 1. Without RESTful and Without Model FBV
    path(
        "FBV_WithoutRESTfulAndWithoutModel/",
        views.FBV_WithoutRESTfulAndWithoutModel,
        name="FBV_WithoutRESTfulAndWithoutModel",
    ),
    # 2. Without RESTful and With Model FBV
    path(
        "FBV_WithoutRESTfulAndWithModel/",
        views.FBV_WithoutRESTfulAndWithModel,
        name="FBV_WithoutRESTfulAndWithModel",
    ),
]

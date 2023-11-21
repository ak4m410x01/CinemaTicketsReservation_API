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
    # 3. With RESTful and With Model List Guests FBV
    path(
        "FBV_WithRESTfulAndWithModelListGuests/",
        views.FBV_WithRESTfulAndWithModelListGuests,
        name="FBV_WithRESTfulAndWithModelListGuests",
    ),
    # 4. With RESTful and With Model Create Guest FBV
    path(
        "FBV_WithRESTfulAndWithModelCreateGuest/",
        views.FBV_WithRESTfulAndWithModelCreateGuest,
        name="FBV_WithRESTfulAndWithModelCreateGuest",
    ),
]

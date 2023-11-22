from django.urls import path
from tickets import views

app_name = "tickets"

urlpatterns = [
    # 1. FBV Without Model and Without RESTful
    path(
        "fbv/withoutmodel/withoutrest/",
        views.fbv_withoutModel_withoutRESTful,
        name="fbv_withoutModel_withoutRESTful",
    ),
    # 2. FBV With Model and Without RESTful
    path(
        "fbv/withmodel/withoutrest/",
        views.fbv_withModel_withoutRESTful,
        name="fbv_withModel_withoutRESTful",
    ),
    # 3. FBV With Model and With RESTful List Guests
    path(
        "fbv/withmodel/withrest/list/guests/",
        views.fbv_withModel_withRESTful_listGuests,
        name="fbv_withModel_withRESTful_listGuests",
    ),
    # 4. FBV With Model and With RESTful List Guest
    path(
        "fbv/withmodel/withrest/list/guest/<int:pk>/",
        views.fbv_withModel_withRESTful_listGuest,
        name="fbv_withModel_withRESTful_listGuest",
    ),
    # 5. FBV With Model and With RESTful Create Guest
    path(
        "fbv/withmodel/withrest/create/guest/",
        views.fbv_withModel_withRESTful_createGuest,
        name="fbv_withModel_withRESTful_createGuest",
    ),
    # 6. FBV With Model and With RESTful Update Guest
    path(
        "fbv/withmodel/withrest/update/guest/<int:pk>/",
        views.fbv_withModel_withRESTful_updateGuest,
        name="fbv_withModel_withRESTful_updateGuest",
    ),
]

from django.urls import path, include
from tickets import views
from tickets.routers import router

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
    # 7. FBV With Model and With RESTful Delete Guest
    path(
        "fbv/withmodel/withrest/delete/guest/<int:pk>/",
        views.fbv_withModel_withRESTful_deleteGuest,
        name="fbv_withModel_withRESTful_deleteGuest",
    ),
    # 8. CBV With Model and With RESTful List And Create Guests
    path(
        "cbv/withmodel/withrest/list/guests/",
        views.CBVWithModelWithRESTfulListAndCreateGuest.as_view(),
        name="CBVWithModelWithRESTfulListAndCreateGuest",
    ),
    # 9. CBV With Model and With RESTful Get And Update And Delete Guest
    path(
        "cbv/withmodel/withrest/guest/<int:pk>/",
        views.CBVWithModelWithRESTfulGetAndUpdateAndDeleteGuest.as_view(),
        name="CBVWithModelWithRESTfulGetAndUpdateAndDeleteGuest",
    ),
    # 10. Mixins With Model and With RESTful List And Create Guest
    path(
        "mixins/withmodel/withrest/list/guests/",
        views.MixinsWithModelWithRESTfulListAndCreateGuest.as_view(),
        name="MixinsWithModelWithRESTfulListAndCreateGuest",
    ),
    # 11. Mixins With Model and With RESTful Get And Update And Delete Guest
    path(
        "mixins/withmodel/withrest/guest/<int:pk>/",
        views.MixinsWithModelWithRESTfulGetAndUpdateAndDeleteGuest.as_view(),
        name="MixinsWithModelWithRESTfulGetAndUpdateAndDeleteGuest",
    ),
    # 12. Generics With Model and With RESTful List And Create Guest
    path(
        "generics/withmodel/withrest/list/guests/",
        views.GenericsWithModelWithRESTfulListAndCreateGuest.as_view(),
        name="GenericsWithModelWithRESTfulListAndCreateGuest",
    ),
    # 13. Generics With Model and With RESTful Get And Update And Delete Guest
    path(
        "generics/withmodel/withrest/guest/<int:pk>/",
        views.GenericsWithModelWithRESTfulGetAndUpdateAndDeleteGuest.as_view(),
        name="GenericsWithModelWithRESTfulGetAndUpdateAndDeleteGuest",
    ),
    # 14. Viewsets With Model and With RESTful List, Create, Get, Update, and Delete Guest
    path(
        "viewsets/withmodel/withrest/",
        include(router.urls),
    ),
    # search guest by fn
    path(
        "fbv/search-guest",
        views.searchGuest,
    ),
]

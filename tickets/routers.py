from rest_framework.routers import DefaultRouter
from tickets import views

router = DefaultRouter()
router.register(
    "guest/vws",
    views.ViewsetsWithModelWithRESTfulListAndCreateAndGetAndUpdateAndDeleteGuest,
)

router.register("guests", views.GuestViewSet)
router.register("movies", views.MovieViewSet)
router.register("reservations", views.ReservationViewSet)
router.register("posts", views.PostsViewSet)

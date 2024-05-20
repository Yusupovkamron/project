from django.urls import path, include
from .views import SweetsListView, UsersLoginView, MastersSetView, DiscountsView, RegisterApiView, LocationsView, ClientsViewApiSet, UserRegisterView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("clients", viewset=ClientsViewApiSet)
# from drf_yasg.view import get_schema_view
# from drf_yasg import openapi
# schema_view = get_schema_view(
#     openapi.INFO(
#         title="SWEET API",
#         description="SWEET Applications demo",
#         default_version='v1',
#         terms_of_service="demo.com",
#         contact=openapi.Contact(email="kamron@gamil.com"),
#         license=openapi.License(name="demo service")
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny, ]
# )



urlpatterns = [
    path("", SweetsListView.as_view(), name="home"),
    path("login/", UsersLoginView.as_view(), name="login"),
    path("clients/", ClientsViewApiSet.as_view(), name="clients"),
    path("masters/", MastersSetView.as_view(), name="master"),
    path("discounts/", DiscountsView.as_view(), name="discounts"),
    path("locations/", LocationsView.as_view(), name="locations"),
    # path("docs/", schema_view.with_ue ("swagger", cashe_timeout=0), namae='swagger'),
    path("register/", RegisterApiView.as_view(), name="register"),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
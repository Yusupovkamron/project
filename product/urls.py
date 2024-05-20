from django.urls import path
from .views import ProductsApiView

urlpatterns = [
    path("product/", ProductsApiView.as_view(), name="product"),
    path("server/", ProductsApiView.as_view(), name="server"),
]
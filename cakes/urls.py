from django.urls import path
from .views import SweetsListView
urlpatterns = [
    path("", SweetsListView.as_view(), name="home"),
    path("login/", SweetsListView.as_view(), name="login"),
    path("about.html/", SweetsListView.as_view(), name="about.html"),
    path("menu.html/", SweetsListView.as_view(), name="menu.html"),
    path("team.html/", SweetsListView.as_view(), name="team.html"),
]
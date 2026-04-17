"""Backend URL Configuration."""

from django.contrib import admin
from django.urls import include, path

from backend.pages.views import (
    AboutUsView,
    ContactUsView,
    HomePageView,
)
from backend.video.views import (
    meet_view,
    new_meet_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("new/", new_meet_view),
    path("accounts/", include("backend.accounts.urls")),
    path("<uuid:room_id>/", meet_view),
    path("", HomePageView.as_view(), name="home"),
    path("contact-us/", ContactUsView.as_view(), name="contact-us"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
]

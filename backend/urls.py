"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (
    path,
    include,
    re_path
)

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from backend.video.views import (
    meet_view,
    new_meet_view,
)

from backend.pages.views import (
    HomePageView,
    ContactUsView,
    AboutUsView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', new_meet_view),
    path('accounts/', include('backend.accounts.urls')),
    path('<uuid:room_id>/', meet_view),

    path('', HomePageView.as_view(), name='home'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

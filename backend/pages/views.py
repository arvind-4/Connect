"""Views for the pages."""

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Home page view."""

    template_name = "pages/home-page.html"


class ContactUsView(TemplateView):
    """Contact us page view."""

    template_name = "pages/contact-us.html"


class AboutUsView(TemplateView):
    """About us page view."""

    template_name = "pages/about-us.html"

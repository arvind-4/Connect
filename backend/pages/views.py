from django.shortcuts import render
from django.views.generic import TemplateView

# def home_page(request):
#     return render(request, 'pages/home-page.html', context={})

class HomePageView(TemplateView):
    template_name = 'pages/home-page.html'

class ContactUsView(TemplateView):
    template_name = 'pages/contact-us.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about-us.html'
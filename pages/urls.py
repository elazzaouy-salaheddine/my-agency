from django.urls import path
from .views import homepage,faqs, contact, Portfolio,about, services

app_name = 'home_page'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('faqs/', faqs, name='faqs'),
    path('contact/', contact, name='contact'),
    path('portfolio/', Portfolio, name='portfolio'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
]

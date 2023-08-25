from django.urls import path
from django.views.generic import TemplateView
from .views import PortfolioViews, PorfolioDetailView
app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioViews, name='projects'),
    path('<id>/', PorfolioDetailView, name='projectdetails' ),

]

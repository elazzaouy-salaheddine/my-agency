from django.shortcuts import get_object_or_404, redirect, render

from portfolio.models import Portfolio
# Create your views here.
def homepage(request):
    context = {}
    return render(request,"pages/home.html", context)

# Faqs

def faqs(request):
    context = {}
    return render(request, 'pages/faqs.html', context)
# contact

def contact(request):
    context = {
        'page_title':'contact us',
    }
    return render(request, 'pages/contact.html', context)
# recent work

def services(request):
    context = {
        'page_title':'our services',
    }
    return render(request, 'pages/services.html', context)
# about

def about(request):
    return render(request, 'pages/about.html')

# meet our team 
def Portfolio(request):
    return render(request, 'pages/portfolio.html')


def PortfolioDetailViews(request, id):
    project = Portfolio.objects.get(id = id)

    return render(request, 'pages/portfolio_detail.html')
# what we offer
# latest news blog
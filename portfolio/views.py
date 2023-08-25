from django.shortcuts import get_object_or_404, redirect, render
from .models import Portfolio


def PortfolioViews(request):
    context ={}
 
    # add the dictionary during initialization
    projects = Portfolio.objects.all()
    context ={
        'projects':projects,
        'page_title':'our projects',
    }
    return render(request, 'pages/portfolio.html', context)


def PorfolioDetailView(request, id):
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Portfolio.objects.get(id = id)
         
    return render(request, "pages/porfolio_detail_view.html", context)

from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail

from portfolio.models import Portfolio
from blog.models import Post
# Create your views here.
def homepage(request):
    context ={}
    posts = Post.objects.all()[:3]
    context ={
        'posts':posts,
    }
    return render(request,"pages/home.html", context)

# Faqs

def faqs(request):
    context = {}
    return render(request, 'pages/faqs.html', context)
# contact

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Phone:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
        send_mail('mail from agency', message, '', ['nisozagency@gmail.com']) # TODO: enter your email address
        return redirect('homepage')
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
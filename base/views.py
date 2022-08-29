from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .models import *
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, "index.html")


def projects(request):
    # projects = {'projects' : Project.objects.all()}
    return render(request, "projects.html")

def designs(request):
    context = {'designs' : Design.objects.all()}
    return render(request, "designs.html", context)

def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            linkedin = form.cleaned_data['linkedin']
            message = form.cleaned_data['message']

            html = render_to_string('email.html', {
                'name': name,
                'subject': subject,
                'email': email,
                'linkedin':linkedin,
                'message': message
            })

            send_mail(subject, message, email, ['dfntlynotace@gmail.com', 'avishkakavindagamage@gmail.com'], html_message=html)

            return redirect('about')
    else:
        form = ContactForm()

    return render(request, "about.html", {
        'form': form
    })

def mind(request):
    return render(request, "mind.html")
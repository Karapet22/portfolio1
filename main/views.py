from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail

from TaleSeoAgency.settings import EMAIL_HOST_USER
from .models import Contacts, Services, ServiceType, Projects, ProjectType, Head, AboutUs
from .forms import ContactForm

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        context = {
            'contacts': Contacts.objects.get(),
            'service': Services.objects.get(),
            "servicetypes": ServiceType.objects.all(),
            'project': Projects.objects.get(),
            'projecttype': ProjectType.objects.all(),
            'head': Head.objects.get(),
            'about_us': AboutUs.objects.get(),
        }

        return render(request, self.template_name, context=context)
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                from_email=EMAIL_HOST_USER,
                recipient_list=[request.POST["email"]],
                subject="Confirmation Email",
                message="We Got You Message, Wait for review!!!",
            )
            form.save()
            return redirect('/')
        else:
            form = ContactForm()
            return redirect('/')


class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name)
    


class FAQsListView(ListView):
    template_name = 'faqs.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name)
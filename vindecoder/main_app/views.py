from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import FormMixin
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import FormView
from .forms import ContactForm
from .models import Vincode
from django.db.models import Q

class HomePage(FormMixin,ListView):
    model=Vincode
    template_name="home.html"
    form_class = ContactForm
    context_object_name="object"
    success_url = '/'
    def get_queryset(self):
        result=""
        query = self.request.GET.get('q')
        if query:
            result = Vincode.objects.filter(
                       Q(vin__icontains=query) 
            )
        return result

    def post(self, request, **kwargs):
        subject=self.request.POST.get("subject")
        message=self.request.POST.get("message")
        email=self.request.POST.get("email")
        send_mail(
            subject,
            message,
            email,
            ['elvinc402@gmail.com'],
        )
        return redirect("main_app:home")

    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def form_valid(self,form):
        print(form)
        print(self.request.POST)

        subject=form.cleaned_data.get("subject")
        message=form.cleaned_data.get("message")
        email=form.cleaned_data.get("email")
        send_mail(
            subject,
            message,
            email,
            ['elvinc402@gmail.com'],
        )
      
        return super().form_valid(form)


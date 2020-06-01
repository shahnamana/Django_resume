from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.
from .models import *


class HouseTemplateView(TemplateView):
    template_name = 'home.html'

    #override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #first, get super get context
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        context['certificate'] = Certificate.objects.all()
        return context

#
# def contact(request):
#
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']
#
#         return render(request, "home.html", {'name':name})
#     else:
#         pass
#

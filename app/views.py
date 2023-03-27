from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render,redirect;
from .models import *
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
# Create your views here.
def index(request):
   return render(request,'index.html')

class HomeTemplateView(TemplateView):
   template_name="home.html"

   def get_context_data(self,**kwargs):
      context=super().get_context_data(**kwargs)
      context['about']=About.objects.first()
      context['services']=Service.objects.all()
      context['works']=RecentWork.objects.all()
      return context
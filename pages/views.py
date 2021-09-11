from django.shortcuts import render
from django.http import HttpResponse
from . import models


from django.views import generic
from django.views.generic.edit import CreateView

class HomePageView(generic.TemplateView):
    template_name="home.html"

# def index(response, id):
#         ls = ToDoList.objects.get(id=id)
#         return render(response,"main/list.html",{"ls":ls})

# def home(response):
#     return render(response, "main/home.html",{})

class create(CreateView): 
    model = models.User
    template_name = "main/create.html"
    fields = [ "Company_Name", "InterestRateAfterDefault"]
  

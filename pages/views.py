from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.db.models import Sum
from django.views import generic
from django.views.generic.edit import CreateView

class HomePageView(generic.TemplateView):
    template_name="home.html"

class ListView(generic.ListView):
    model = models.User
    template_name="main/list.html"

class DataVizView(generic.ListView):
    model = models.User
    template_name="main/dataviz.html"
    def get_context_data(self, **kwargs):
        context = super(DataVizView, self).get_context_data(**kwargs)
        # context['Loan_Rate_After_Default_sum'] = models.User.objects.all().aggregate(sum_all=Sum('Loan_Rate_After_Default')).get('sum_all')
        context['Loan_Rate_After_Default_sum'] = models.User.objects.all().aggregate(Sum('Loan_Rate_After_Default'))
        return context

 



# SELECT AVG(Initial_Loan_Amount)
# Initial_Interest_Rate

# Loan_Duration 
# Final_Loan_Amount 
# Overall_Rating 
    
        # def get_queryset(self):
        #     return Project.objects

# def index(response, id):
#         ls = ToDoList.objects.get(id=id)
#         return render(response,"main/list.html",{"ls":ls})

# def home(response):
#     return render(response, "main/home.html",{})

class create(CreateView): 
    model = models.User
    template_name = "main/create.html"
    fields = ["Company_Name", "Initial_Loan_Amount", "Initial_Interest_Rate", 
    "Loan_Rate_After_Default", "Loan_Duration", "Final_Loan_Amount", "Overall_Rating"]

    
  

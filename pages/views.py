from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.http import HttpResponse

def homePageView(request):
  return HttpResponse('Hello, World!')
>>>>>>> 8a2aa610a603a883ab177acd12df18effcad3f2a

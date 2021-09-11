from django.urls import path, include
from .views import HomePageView
from . import views

urlpatterns = [
   #path("<int:id>", views.index, name="index"),
    path('', HomePageView.as_view(), name='home'),
    path("create/", views.create.as_view(), name='create'),
]
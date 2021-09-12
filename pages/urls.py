from django.urls import path, include
from .views import HomePageView, ListView, DataVizView
from . import views
from django.contrib import admin

urlpatterns = [
   #path("<int:id>", views.index, name="index"),
    path('', HomePageView.as_view(), name='home'),
    path("create/", views.create.as_view(), name='create'),
    path('list/', ListView.as_view(), name='list'),
    path('dataviz/', DataVizView.as_view(), name='dataviz'),
    path('admin/',admin.site.urls)
]
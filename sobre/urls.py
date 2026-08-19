from django.urls import path 

from . import views 

urlpatterns = [ 
    path("", views.meus_dados, name="meus_dados"), 

] 
from django.urls import path
from . import views

urlpatterns = [

    path('sending_individual_mail', views.individual_mail),
]

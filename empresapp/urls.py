from django.urls import path 

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("tarifas",views.tarifas),
    path("tos",views.tos),
    path("about",views.about),
]
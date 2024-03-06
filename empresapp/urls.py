from django.urls import path 

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("tarifas",views.tarifas,name="tarifas"),
    path("reservar",views.reservar,name="reservar"),
    path("tos",views.tos,name="tos"),
    path('logout',views.logout,name="logout"),
    path('login',views.login,name="login"),
    path("about",views.about,name="about"),
]
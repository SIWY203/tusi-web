from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('o_nas/', views.o_nas, name='o_nas'),
    path('aktualnosci/', views.aktualnosci, name='aktualnosci'),
    path('oferta/', views.oferta, name='oferta'),
    path('galeria/', views.galeria, name='galeria'), 
    path('kontakt/', views.kontakt, name='kontakt'), 
    path('oferta/<slug:slug>/', views.oferta_podstrona, name='oferta_podstrona'),
    path('cennik/', views.cennik, name='cennik'),

]


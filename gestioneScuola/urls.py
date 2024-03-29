from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="gestioneScuola"
urlpatterns=[
  path('',views.index,name="index"),
  path('aggiungiVoto/',views.aggiungiVoto,name="aggiungiVoto"),
  path('rimuoviVoto/',views.rimuoviVoto,name="rimuoviVoto"),
  path('modificaVoto/',views.modificaVoto,name="modificaVoto"),
  path('aggiungiCompito/',views.aggiungiCompito,name='aggiungiCompito'),
  path('compitiDaFare/',views.compitiDaFare,name='compitiDaFare'),
  path('rimuoviCompito/',views.rimuoviCompito,name='rimuoviCompito'),
  path('login/',auth_views.LoginView.as_view(template_name="login.html"),name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name="logout.html"),name='logout'),
]
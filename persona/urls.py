from django.urls import path
from persona import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.prueba),
    path('hola', views.Hola.as_view(), name="hola"),
    path('saludo', views.Saludo.as_view(), name="Saludo"),
    path('saludo2', views.SaludoDos.as_view(), name="SaludoDos"),
    path('saludo3', views.Saludo.as_view(saludo="saludo desde url"), name="SaludoTres"),
    path('prueba_login', login_required(views.PruebaLogin.as_view()), name="prueba_login"),
    path('prueba_login_dos', login_required(views.PruebaLoginDos.as_view()), name="prueba_login_dos"),
    path("index", views.Index.as_view(), name="index"),
    path("nueva_persona", views.CreatePersona.as_view()),
    path("listar_personas", views.ListarPersonas.as_view(), name="listado"),
    path("editar_persona/<int:pk>", views.UpdatePersona.as_view()),
    path("persona/<int:pk>", views.VerPersona.as_view()),
    path("borrar_persona/<int:pk>", views.BorrarPersona.as_view()),
]

from django.shortcuts import render, HttpResponse, redirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views import View

# Create your views here.
def prueba(request):
    return render(request, "prueba.html", {})


class Hola(View):
    def get(self, request):
        return HttpResponse("Hola desde Get")

    def post(self, request):
        return HttpResponse("Hola desde Post")

class Saludo(View):
    saludo = "HOLA"
    def get(self, request):
        return HttpResponse(self.saludo)

class SaludoDos(Saludo):
    saludo = "saludo dos"


class PruebaLogin(View):
    def get(self, request):
        return HttpResponse(self.saludo)


@method_decorator(login_required, name="dispatch")
class PruebaLoginDos(View):
    def get(self, request):
        return HttpResponse(self.saludo)


from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Index,self).get_context_data(*args, **kwargs)
        context["nombre"] = "axel"
        return context


from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from .forms import PersonaForm
from .models import Persona
from django.urls import reverse_lazy

class CreatePersona(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = "nueva_persona.html"
    success_url = reverse_lazy("listado")

class ListarPersonas(ListView):
    model = Persona
    template_name = "lista_persona.html"
    paginate_by = 10
    #queryset = Persona.objects.filter(nombre="axel")
    #def get_queryset(self):
        #query = Persona.objects.filter(nombre="axel")
        #return query

class UpdatePersona(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = "nueva_persona.html"
    success_url = reverse_lazy("listado")

class VerPersona(DetailView):
    model = Persona
    template_name = "persona.html"

class BorrarPersona(DeleteView):
    model = Persona
    template_name = "borrar_persona.html"
    success_url = reverse_lazy("listado")
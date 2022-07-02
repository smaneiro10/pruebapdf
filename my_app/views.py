from django.shortcuts import render
#
from django.http import HttpResponse
#
from .models import Empleado
#
from .utils import render_to_pdf
#
from django.views.generic import ListView, View


# Create your views here.

class ListaEmpleadosListView(ListView):
    model = Empleado
    template_name = 'lista_empleados.html'
    context_object_name = 'pelados'


# Create your views here.
class ListEmpleadosPdf(View):

    def get(self, request, *args, **kwargs):
        empleados = Empleado.objects.all()
        data = {
            'count': empleados.count(),
            'empleados': empleados
        }
        pdf = render_to_pdf('lista_empleadospdf.html', data)
        return HttpResponse(pdf, content_type='my_app/pdf')
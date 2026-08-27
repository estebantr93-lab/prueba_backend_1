from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .servicios import obtener_zonas_con_resumen, obtener_detalle_zona

def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }
    return render(request, "dispositivos/inicio.html", contexto)

def dispositivos_zona(request, zona_id):
    if zona_id != 3:
        return HttpResponse("Zona no encontrada", status=404)
    return HttpResponse(f"Dispositivos de la zona {zona_id}")

def dispositivos_id(request, dispositivo_id):
    if dispositivo_id != 7:
        return HttpResponse("Dispositivo no encontrado", status=404)
    return HttpResponse(f"Dispositivo {dispositivo_id} encontrado")

def catalogo(request):
    dispositivos = [
        {"nombre": "Medidor inteligente", "estado": "Activo"},
        {"nombre": "Sensor de temperatura", "estado": "Activo"},
        {"nombre": "Climatizador", "estado": "Revisión"}
    ]
    return render(request, "dispositivos/catalogo.html", {"dispositivos": dispositivos})

def listado_zonas(request):
    zonas = obtener_zonas_con_resumen()
    contexto = {
        'zonas': zonas,
    }
    return render(request, 'dispositivos/zonas_listado.html', contexto)


def detalle_zona(request, zona_id):
    detalle = obtener_detalle_zona(zona_id)

    if detalle is None:
        raise Http404('La zona solicitada no existe.')

    contexto = {
        'zona': detalle['zona'],
        'dispositivos': detalle['dispositivos'],
        'consumo_total': detalle['consumo_total'],
        'estado': detalle['estado'],
    }
    return render(request, 'dispositivos/zona_detalle.html', contexto)
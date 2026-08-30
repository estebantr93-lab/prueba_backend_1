from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .servicios import obtener_zonas_con_resumen, obtener_detalle_zona, obtener_zonas, obtener_dispositivos

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

def resumen_zonas(request):
    zonas = obtener_zonas()
    dispositivos = obtener_dispositivos()

    resumen = []
    consumo_general = 0

    for zona in zonas:
        dispositivos_zona = [d for d in dispositivos if d['zona_id'] == zona['id']]
        consumo_total = sum(d['consumo_kwh'] for d in dispositivos_zona)

        if consumo_total > zona['limite_kwh']:
            estado = 'LÍMITE SUPERADO'
            clase_estado = 'danger'
        else:
            estado = 'DENTRO DEL LÍMITE'
            clase_estado = 'success'

        resumen.append({
            'id': zona['id'],
            'nombre': zona['nombre'],
            'cantidad_dispositivos': len(dispositivos_zona),
            'consumo_total': consumo_total,
            'limite_kwh': zona['limite_kwh'],
            'estado': estado,
            'clase_estado': clase_estado,
        })

        consumo_general += consumo_total

    contexto = {
        'resumen': resumen,
        'total_zonas': len(zonas),
        'total_dispositivos': len(dispositivos),
        'consumo_general': consumo_general,
    }
    return render(request, 'dispositivos/resumen_zonas.html', contexto)
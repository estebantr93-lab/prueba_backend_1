import json
from django.conf import settings

DATA_DIR = settings.BASE_DIR / 'dispositivos' / 'data'


def _cargar_json(nombre_archivo):
    ruta = DATA_DIR / nombre_archivo
    with open(ruta, encoding='utf-8') as f:
        return json.load(f)


def obtener_zonas():
    return _cargar_json('zonas.json')


def obtener_categorias():
    return _cargar_json('categorias.json')


def obtener_dispositivos():
    return _cargar_json('dispositivos.json')


def obtener_zona_por_id(zona_id):
    zonas = obtener_zonas()
    for zona in zonas:
        if zona['id'] == zona_id:
            return zona
    return None


def obtener_dispositivos_de_zona(zona_id):
    dispositivos = obtener_dispositivos()
    return [d for d in dispositivos if d['zona_id'] == zona_id]


def obtener_categoria_por_id(categoria_id):
    categorias = obtener_categorias()
    for c in categorias:
        if c['id'] == categoria_id:
            return c
    return None


def calcular_consumo_total(dispositivos_zona):
    return sum(d['consumo_kwh'] for d in dispositivos_zona)


def calcular_estado(consumo_total, limite_kwh):
    return 'ALERTA' if consumo_total > limite_kwh else 'NORMAL'


def obtener_zonas_con_resumen():
    """Para el listado: cada zona con su cantidad de dispositivos."""
    zonas = obtener_zonas()
    resultado = []
    for zona in zonas:
        dispositivos_zona = obtener_dispositivos_de_zona(zona['id'])
        resultado.append({
            **zona,
            'cantidad_dispositivos': len(dispositivos_zona),
        })
    return resultado


def obtener_detalle_zona(zona_id):
    """Para el detalle: zona + sus dispositivos con categoría, consumo total y estado."""
    zona = obtener_zona_por_id(zona_id)
    if zona is None:
        return None

    dispositivos_zona = obtener_dispositivos_de_zona(zona_id)

    dispositivos_con_categoria = []
    for d in dispositivos_zona:
        categoria = obtener_categoria_por_id(d['categoria_id'])
        dispositivos_con_categoria.append({
            **d,
            'categoria_nombre': categoria['nombre'] if categoria else 'Sin categoría',
        })

    consumo_total = calcular_consumo_total(dispositivos_zona)
    estado = calcular_estado(consumo_total, zona['limite_kwh'])

    return {
        'zona': zona,
        'dispositivos': dispositivos_con_categoria,
        'consumo_total': consumo_total,
        'estado': estado,
    }
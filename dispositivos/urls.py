# dispositivos/urls.py
from django.urls import path
from . import views

app_name = "dispositivos"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("zonas/<int:zona_id>/dispositivos/", views.dispositivos_zona, name="por_zona"),
    path("dispositivos/", views.catalogo, name="catalogo"),  
    path("dispositivos/<int:dispositivo_id>/", views.dispositivos_id),  
    path('zonas/', views.listado_zonas, name='listado_zonas'),
    path('zonas/<int:zona_id>/', views.detalle_zona, name='detalle_zona'),
    path('resumen-zonas/', views.resumen_zonas, name='resumen_zonas'),
]



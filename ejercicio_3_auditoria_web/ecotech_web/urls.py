# Asociamos la direccion principal con la vista del panel.
from django.urls import path
from sustentabilidad.views import vista_panel_sustentabilidad

urlpatterns = [
    path("", vista_panel_sustentabilidad, name="panel_sustentabilidad"),
]

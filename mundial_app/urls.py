from django.urls import path

from mundial_app import views


urlpatterns = [
    path('equipo/<int:id>', views.mostrarEquipo),
    path('equipos', views.mostrarEquipos)
]
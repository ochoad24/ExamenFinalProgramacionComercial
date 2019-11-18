from django.urls import path
from . import views
urlpatterns = [
    path('', views.grado_nuevo, name='grado_nuevo'),
]
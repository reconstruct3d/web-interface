from django.urls import path

from . import views
from . import reconstruct

urlpatterns = [
    path('', views.index, name='index'),
    path('perform', views.perform, name='perform'),
    path('reconstruct', reconstruct.reconstruct, name='reconstruct'),
]
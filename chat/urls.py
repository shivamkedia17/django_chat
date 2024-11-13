from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby),
    # path('lobby.js', lambda request: render())
]

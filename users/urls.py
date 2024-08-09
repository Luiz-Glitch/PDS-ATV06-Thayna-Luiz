from django.urls import path
from .views import luiz, taina



urlpatterns = [
    path("luiz", luiz, name="luiz"),
    path("taina", taina, name="taina"),
]
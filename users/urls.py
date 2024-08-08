from django.urls import path
from .views import luiz

urlpatterns = [
    path("luiz", luiz, name="luiz"),
]
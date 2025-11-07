from django.urls import path
from .introspection import token_introspect

urlpatterns = [
    path('api/token/introspect/', token_introspect),
]

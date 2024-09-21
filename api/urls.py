from django.urls import path
from .views import collection_request, entity_request

urlpatterns = [
  path('users/', collection_request),
  path('users/<int:id>', entity_request)
]
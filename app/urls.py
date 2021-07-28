from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, CursoViewSet

router = DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('cursos', CursoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
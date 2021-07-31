from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import BeneficioViewSet, CategoriaViewSet, CursoBeneficioViewSet, CursoViewSet, HorarioCursoViewSet, HorarioViewSet, SemanaViewSet, SesionViewSet

router = DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('cursos', CursoViewSet)
router.register('sesiones', SesionViewSet)
router.register('semanas', SemanaViewSet)
router.register('horarios', HorarioViewSet)
router.register('horario-cursos', HorarioCursoViewSet)
router.register('beneficios', BeneficioViewSet)
router.register('curso-beneficios', CursoBeneficioViewSet)

urlpatterns = [
    path('', include(router.urls))
]
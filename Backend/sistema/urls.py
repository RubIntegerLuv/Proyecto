from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet, TrabajadorViewSet, DocumentoViewSet, DatosDinamicosView

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'trabajadores', TrabajadorViewSet)
router.register(r'documentos', DocumentoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/datos_dinamicos/', DatosDinamicosView.as_view(), name='datos-dinamicos'),
]

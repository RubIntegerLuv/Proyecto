from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Empresa, Trabajador, Documento
from .serializers import EmpresaSerializer, TrabajadorSerializer, DocumentoSerializer
import json


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


class DatosDinamicosView(APIView):
    """
    Endpoint para consultas dinámicas con soporte para múltiples valores en los filtros.
    """

    def get(self, request):
        selected_columns = request.GET.getlist('columns', [])
        filters = request.GET.get('filters', '{}')

        try:
            filters = json.loads(filters)
        except ValueError:
            filters = {}

        combined_results = []

        # Procesar filtros con múltiples valores
        processed_filters = {}
        for key, value in filters.items():
            try:
                processed_filters[key] = json.loads(value)  # Convierte los valores JSON a listas
            except (ValueError, TypeError):
                processed_filters[key] = [value]  # Si falla, tratar como un único valor

        # Detectar tablas involucradas
        include_empresa = any(col in ['id_empresa', 'nombre_empresa', 'rubro'] for col in selected_columns)
        include_trabajador = any(col in ['id_trabajador', 'nombre_trabajador', 'cargo', 'empresaID'] for col in selected_columns)
        include_documento = any(col in ['id_documento', 'tipo', 'fecha', 'trabajadorID'] for col in selected_columns)

        # Combinar datos según relaciones
        if include_empresa:
            empresas = Empresa.objects.prefetch_related('trabajadores__documentos')

            for empresa in empresas:
                base_row = {
                    'id_empresa': empresa.id if 'id_empresa' in selected_columns else None,
                    'nombre_empresa': empresa.nombre_empresa if 'nombre_empresa' in selected_columns else None,
                    'rubro': empresa.rubro if 'rubro' in selected_columns else None,
                }

                if include_trabajador:
                    for trabajador in empresa.trabajadores.all():
                        trabajador_row = {
                            'id_trabajador': trabajador.id if 'id_trabajador' in selected_columns else None,
                            'nombre_trabajador': trabajador.nombre_trabajador if 'nombre_trabajador' in selected_columns else None,
                            'cargo': trabajador.cargo if 'cargo' in selected_columns else None,
                        }

                        if include_documento:
                            for documento in trabajador.documentos.all():
                                documento_row = {
                                    'id_documento': documento.id if 'id_documento' in selected_columns else None,
                                    'tipo': documento.tipo if 'tipo' in selected_columns else None,
                                    'fecha': documento.fecha if 'fecha' in selected_columns else None,
                                }
                                combined_results.append({**base_row, **trabajador_row, **documento_row})
                        else:
                            combined_results.append({**base_row, **trabajador_row})
                else:
                    combined_results.append(base_row)

        elif include_trabajador:
            trabajadores = Trabajador.objects.prefetch_related('documentos', 'empresa')

            for trabajador in trabajadores:
                trabajador_row = {
                    'id_trabajador': trabajador.id if 'id_trabajador' in selected_columns else None,
                    'nombre_trabajador': trabajador.nombre_trabajador if 'nombre_trabajador' in selected_columns else None,
                    'cargo': trabajador.cargo if 'cargo' in selected_columns else None,
                }

                if include_documento:
                    for documento in trabajador.documentos.all():
                        documento_row = {
                            'id_documento': documento.id if 'id_documento' in selected_columns else None,
                            'tipo': documento.tipo if 'tipo' in selected_columns else None,
                            'fecha': documento.fecha if 'fecha' in selected_columns else None,
                        }
                        combined_results.append({**trabajador_row, **documento_row})
                else:
                    combined_results.append(trabajador_row)

        elif include_documento:
            documentos = Documento.objects.prefetch_related('trabajador__empresa')

            for documento in documentos:
                documento_row = {
                    'id_documento': documento.id if 'id_documento' in selected_columns else None,
                    'tipo': documento.tipo if 'tipo' in selected_columns else None,
                    'fecha': documento.fecha if 'fecha' in selected_columns else None,
                }

                trabajador = documento.trabajador
                trabajador_row = {
                    'id_trabajador': trabajador.id if trabajador else None,
                    'nombre_trabajador': trabajador.nombre_trabajador if trabajador and 'nombre_trabajador' in selected_columns else None,
                    'cargo': trabajador.cargo if trabajador and 'cargo' in selected_columns else None,
                }

                empresa = trabajador.empresa if trabajador else None
                empresa_row = {
                    'id_empresa': empresa.id if empresa else None,
                    'nombre_empresa': empresa.nombre_empresa if empresa and 'nombre_empresa' in selected_columns else None,
                    'rubro': empresa.rubro if empresa and 'rubro' in selected_columns else None,
                }

                combined_results.append({**documento_row, **trabajador_row, **empresa_row})

        # Aplicar filtros
        for key, values in processed_filters.items():
            combined_results = [row for row in combined_results if row.get(key) in values]

        return Response(combined_results)

"""Módulo que inicializa el paquete `product`."""

from django.apps import AppConfig


class ProductConfig(AppConfig):
    """Configuración de la aplicación Product."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "product"

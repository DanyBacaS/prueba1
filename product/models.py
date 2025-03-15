"""Módulo que inicializa el paquete `product`."""

from django.db import models


class Category(models.Model):
    """Representa una categoría de productos."""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        """Devuelve una representación en cadena del objeto."""
        return self.name


class Color(models.Model):
    """Modelo que representa un color."""

    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        """Devuelve una representación en cadena del objeto."""
        return self.name


class Size(models.Model):
    """Modelo que representa un tamaño."""

    size = models.CharField(max_length=5, unique=True)

    def __str__(self) -> str:
        """Devuelve una representación en cadena del objeto."""
        return self.size


class Product(models.Model):
    """Modelo que representa un producto."""

    nombre = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)
    supplier = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self) -> str:
        """Devuelve una representación en cadena del objeto."""
        return self.name


class ProductVariant(models.Model):
    """Representa una variante de producto con color y tamaño específicos."""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants",
    )
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        """Define restricciones y metadatos del modelo."""

        unique_together = ("product", "color", "size")

    def __str__(self) -> str:
        """Devuelve una representación en cadena del objeto."""
        return (
            f"{self.product.name} - {self.color.name} - "
            f"{self.size.size} (${self.price})"
        )

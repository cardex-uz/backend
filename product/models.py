from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """ """
    name = models.CharField(verbose_name="Name", max_length=15)
    slug = models.SlugField(verbose_name="Slug", max_length=15, unique=True)

    class Meta:
        db_table = 'category'
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Type(models.Model):
    """ """
    provider = models.ForeignKey(verbose_name="Provider", to="management.Provider", on_delete=models.CASCADE)
    facture = models.CharField(verbose_name="Facture", max_length=10)
    duo = models.BooleanField(verbose_name="Duo", default=False)

    class Meta:
        db_table = "product_type"
        unique_together = [("provider", "facture", "duo"),]
        verbose_name = "Type"
        verbose_name_plural = "Types"


class DeltaPrice(models.Model):
    type = models.ForeignKey(verbose_name="Type", to=Type, on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name="Price", max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "delta_price"
        unique_together = ["type", "created_at"]
        verbose_name = "Delta Price"
        verbose_name_plural = "Delta Prices"


class AbstractProduct:
    """ """
    category = models.ForeignKey(verbose_name="Category", to="Category", on_delete=models.CASCADE)
    front = models.FileField(verbose_name="Front file", upload_to="./")
    back = models.FileField(verbose_name="Back file", upload_to="./")
    front_image = models.ImageField(verbose_name="Front image", upload_to="./")
    back_image = models.ImageField(verbose_name="Back image", upload_to="./")
    mockup = models.ImageField(verbose_name="Mockup", upload_to="./")
    created_at = models.DateTimeField(verbose_name="Created time", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated time", auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class Template(AbstractProduct, models.Model):

    class Meta:
        db_table = "template"
        verbose_name = "Template"
        verbose_name_plural = "Templates"


class Product(AbstractProduct, models.Model):
    customer = models.ForeignKey(verbose_name="Customer", to="management.Customer", on_delete=models.CASCADE)
    front_collage = models.FileField(verbose_name="Front collage", upload_to="./")
    back_collage = models.FileField(verbose_name="Back collage", upload_to="./")

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

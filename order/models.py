from django.db import models

from order.choices import OrderItemStatus, OrderStatus


class Order(models.Model):
    """ """
    customer = models.ForeignKey(verbose_name="Customer", to="management.Customer", on_delete=models.CASCADE)
    provider = models.ForeignKey(verbose_name="Provider", to="management.Provider", on_delete=models.CASCADE)
    cost = models.DecimalField(verbose_name="Cost", max_digits=8, decimal_places=2)
    address = models.CharField(verbose_name="Address", max_length=200)
    status = models.CharField(verbose_name="Status", max_length=10, default=OrderStatus.CREATED, choices=OrderStatus.choices)
    created_at = models.DateTimeField(verbose_name="Created time", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated time", auto_now=True)

    class Meta:
        db_table = 'order'
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderItem(models.Model):
    """ """
    order = models.ForeignKey(verbose_name="Order", to=Order, on_delete=models.CASCADE)
    template = models.ForeignKey(verbose_name="Template", to="product.Template", on_delete=models.CASCADE)
    product = models.ForeignKey(verbose_name="Product", to="product.Product", on_delete=models.CASCADE)
    device = models.ForeignKey(verbose_name="Device", to="management.Device", on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField(verbose_name="Amount", default=1)
    type = models.ForeignKey(verbose_name="Type", to="product.Type", on_delete=models.CASCADE)
    cost = models.DecimalField(verbose_name="Cost", max_digits=8, decimal_places=2)
    status = models.CharField(verbose_name="Status", max_length=10, default=OrderItemStatus.CREATED, choices=OrderItemStatus.choices)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"{self.status}"

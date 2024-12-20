from django.db import models
from django.utils import timezone
from decimal import Decimal
from django.contrib.auth import get_user_model

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Food', 'Food'),
        ('Furniture', 'Furniture'),
        ('Toys', 'Toys'),
    ]

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    added_by = models.ForeignKey(
        get_user_model(), 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='inventory_items'
    )

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('Preparing', 'Preparing'),
        ('Cancelled', 'Cancelled'),
        ('Arrived', 'Arrived')
    ]
    
    id = models.AutoField(primary_key=True)
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, null= True, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Preparing')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.id} - {self.inventory_item.name}"

    class Meta:
        ordering = ['-created_at']


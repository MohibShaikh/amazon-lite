from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from decimal import Decimal # Recommended for price math

# Use the User model you defined correctly
class User(AbstractUser):
    pass

class Product(models.Model):
    # Using type hints (Variable: Type = Field)
    id: uuid.UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name: str = models.CharField(max_length=100)
    description: str = models.TextField()
    stock: int = models.PositiveIntegerField()
    # DecimalField should technically be Decimal for high precision
    price: Decimal = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True)

    @property
    def in_stock(self) -> bool:
        return self.stock > 0

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'

    order_id: uuid.UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status: str = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')

    def __str__(self) -> str:
        return f'Order {self.order_id} by {self.user}'


class OrderItem(models.Model):
    product: Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order: Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity: int = models.PositiveIntegerField()

    @property
    def total(self) -> Decimal:
        # Cast to Decimal/int to ensure the IDE knows the result is a number
        return Decimal(self.product.price) * int(self.quantity)

    def __str__(self) -> str:
        return f'{self.quantity} of {self.product.name} in Order: {self.order}'
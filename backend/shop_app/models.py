from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = User(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        assert extra_fields['is_staff']
        assert extra_fields['is_superuser']
        return self._create_user(email, password, **extra_fields)


USER_TYPE_CHOICES = (
    ('Admin', 'Admin'),
    ('Seller', 'Seller'),
    ('Client', 'Client'),
)


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    user_type = models.CharField(max_length=40, choices=USER_TYPE_CHOICES, default='Client')
    phone_number = models.CharField(max_length=12, null=True)
    street = models.CharField(max_length=32, null=True)
    city = models.CharField(max_length=32, null=True)
    zip_code = models.CharField(max_length=8, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField(null=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()

    def __str__(self):
        return self.product.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'


class Order(models.Model):
    order_status = (
        ('New order', 'New order'),
        ('Waiting for payment', 'Waiting for payment'),
        ('Paid', 'Paid'),
        ('Preparing the order', 'Preparing the order'),
        ('Waiting for Waybill', 'Waiting for Waybill'),
        ('Waiting for the courier', 'Waiting for the courier'),
        ('Sent', 'Sent'),
        ('Cancel', 'Cancel')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=64, choices=order_status, default="New order")
    product = models.ManyToManyField(Product)


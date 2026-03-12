
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    def __str__(self): return self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/',blank=True,null=True)
    rating=models.PositiveSmallIntegerField(default=5)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=30)
    address=models.TextField()
    message=models.TextField(blank=True)
    status=models.CharField(max_length=20,default='pending')
    created_at=models.DateTimeField(auto_now_add=True)

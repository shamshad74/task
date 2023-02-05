from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
class Product(models.Model):
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mobile_number = models.CharField(max_length=20)
    size = models.CharField(max_length=10, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    scraped_at = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to='product_images/')

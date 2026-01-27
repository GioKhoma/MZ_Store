from django.db import models
from django.core.validators import MaxValueValidator


class Product(models.Model):
    CURRENCY_CHOICES = [
        ('GEL', 'GEL'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    ]
        
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()

    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='GEL'
    )

    tags = models.ManyToManyField("products.ProductTag", related_name='products', blank=True)

    def average_rating(self):
        pass


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])


class FavoriteProduct(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)


class ProductTag(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Cart(models.Model):
    products = models.ManyToManyField('products.Product', related_name='carts')
    user = models.OneToOneField('users.User', on_delete=models.SET_NULL, null=True, blank=True)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('products.Product', related_name='images', on_delete=models.CASCADE)
    
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    newest = models.BooleanField(default=False)
    most_populer = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def product_image(self):
        if self.images.all():
            return self.images.all()[0].image

    def get_absolute_url(self):
        return reverse("products:product_detail", args=[self.pk, self.slug])

    def get_add_to_cart_url(self):
        pass

    def get_remove_from_cart_url(self):
        pass


class Image(models.Model):
    image = models.ImageField(upload_to='product', default='avatar.png')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"{self.id}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"

from django.db import models
from datetime import date
from django.contrib.auth.models import User




class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    mfg_date = models.DateField(default=date.today)
    pdt_image = models.ImageField(upload_to='products/')


class Offer(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_percent = models.PositiveIntegerField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class carousalimage(models.Model):
    image=models.ImageField(upload_to='carousal/')

# class footerimage(models.Model):
#     image=models.ImageField(upload_to='footer/')

# class headerimage(models.Model):
#     image=models.ImageField(upload_to='header/')


class fileupload(models.Model):
    image = models.ImageField(upload_to='image/')

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.IntegerField(default=1)

    
class LoginCustomer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)



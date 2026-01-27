from django.db import models
from datetime import date, timezone
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

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    PAYMENT_CHOICES = [
        ('Online', 'Online'),
        ('COD', 'COD'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_CHOICES
    )

    payment_status = models.CharField(
        max_length=20,
        default='Pending'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)



# manager
class DeliveryBoy(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    vehicle_no = models.CharField(max_length=20)
 # ← FIX

class DeliveryBoyOTP(models.Model):
    phone = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at




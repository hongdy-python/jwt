from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=11,unique=True)

    class Meta:
        db_table = "api_user"


class Computer(models.Model):
    name = models.CharField(max_length=30,unique=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    brand = models.CharField(max_length=30,verbose_name="品牌")

    class Meta:
        db_table = 'hdy_computer'
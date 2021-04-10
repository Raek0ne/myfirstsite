from django.db import models

# Create your models here.
class User(models.Model):
    main_id = models.AutoField(primary_key = True)
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 15)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Stock(models.Model):
    main_id = models.AutoField(primary_key = True)
    ticker = models.CharField(max_length = 5)
    quantity = models.IntegerField()
    price = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.ticker
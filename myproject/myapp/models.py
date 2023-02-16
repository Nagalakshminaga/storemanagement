from django.db import models

# Create your models here.
class Store_login(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.TextField()
    

    def __str__(self):
        return self.username
class Store_product(models.Model):
    product_name = models.CharField(max_length=30)
    quantity= models.IntegerField()
    amount = models.TextField()
    delivered= models.IntegerField()
    remaining = models.IntegerField()
    
    def __str__(self):
        return self.product_name


class Store_employee(models.Model):
    employee_name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=30)
    contactno = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return self.employee_name
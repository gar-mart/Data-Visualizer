"""
Definition of models.
"""

from django.contrib import admin
from django.db import models

# Create your models here.
class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name} is {self.age} years old."
    
            
class Car(models.Model):
    # pk    
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=30)
    year = models.IntegerField()
    
    def __str__(self):
        return f"Car is {self.brand} {self.year}"



class Stock(models.Model):
    ticker = models.CharField(max_length=10)
   
    class Meta:
        db_table = '[StockMarket].[Stock]'
    
    def __str__(self):
        return self.ticker



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass



@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass



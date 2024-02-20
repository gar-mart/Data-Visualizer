from pyexpat import model
from django.db import models

# Create your models here.

class LineChart(models.Model):
    YAxis= models.CharField(max_length=100)
    XAxis= models.CharField(max_length=100)
    
    class Meta:
        managed = False



class ConditionColumns(models.Model):
    col = models.CharField(max_length=100)
    operator = models.CharField(max_length=20)
    condition_param = models.CharField(max_length=100)

    def __str__(self):
        return self.col


class ug_TableNames(models.Model):
    table_name = models.CharField(max_length=200)
    ug_table_id = models.IntegerField()

    class Meta:
        managed = False


class ug_TableColumns(models.Model):
    ug_table_id = models.IntegerField()
    column_name = models.CharField(max_length=200)
    data_type = models.CharField(max_length=200)
    
    class Meta:
        managed = False

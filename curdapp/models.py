from django.db import models
class ProductData(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=50)
    pcost=models.IntegerField()
    pcolor=models.CharField(max_length=50)
    pclass=models.CharField(max_length=50)
    cname=models.CharField(max_length=50)
    cmob=models.BigIntegerField()
    cemail=models.EmailField(max_length=50)


# Create your models here.

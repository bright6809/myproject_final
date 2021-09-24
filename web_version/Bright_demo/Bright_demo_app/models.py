from django.db import models

# Create your models here.
class Daycare(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class People(models.Model):
    name=models.CharField(max_length=20)
    gender=models.BooleanField()
    age=models.IntegerField()
    parent_name=models.CharField(max_length=20)
    tel=models.CharField(max_length=12)
    address=models.CharField(max_length=40)
    payment_info=models.CharField(max_length=10)
    teacher=models.CharField(max_length=20)
    memo = models.CharField(max_length=40)

    Daycare_info=models.ForeignKey(Daycare,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


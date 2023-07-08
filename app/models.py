from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Celebraties(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True)
    country=models.CharField(max_length=100)
    field=models.CharField(max_length=100)
    discription=models.TextField()
    photo=models.ImageField(upload_to='p',default=True)
    dob=models.DateField()
    networth=models.IntegerField()

    def __str__(self) -> str:
        return self.name

    
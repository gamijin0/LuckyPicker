from django.db import models

# Create your models here.

class Bot(models.Model):
    #账号
    username = models.CharField(primary_key=True,null=False,max_length=50)
    #cookies
    cookies = models.CharField(max_length=500)



from django.db import models

# Create your models here.

class Bot(models.Model):
    #账号
    username = models.CharField(primary_key=True,null=False,max_length=50)
    #密码
    password = models.CharField(null=False,default="",max_length=50)
    #是否有效
    isValid = models.BooleanField(null=False,default=False)
    #cookies
    cookies = models.CharField(max_length=500)
    #收到的消息数量
    message_num = models.IntegerField(default=0)

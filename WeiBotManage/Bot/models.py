from django.db import models

# Create your models here.

class Bot_db(models.Model):
    #账号
    username = models.CharField(primary_key=True,null=False,max_length=50)
    #密码
    password = models.CharField(null=False,default="",max_length=50)
    #是否有效
    isValid = models.BooleanField(null=False,default=False)
    #cookies
    cookies = models.CharField(max_length=2000)
    #收到的消息数量
    message_num = models.IntegerField(default=0)


class Blogger_db(models.Model):
    #博主账号id
    uid = models.CharField(primary_key=True,null=False,max_length=100)
    #是否已关注
    isCared = models.BooleanField(default=False)


class WeiBo_db(models.Model):
    #微博id
    id = models.CharField(primary_key=True,null=False,max_length=100)
    #所属博主
    blogger = models.ForeignKey(Blogger_db)
    #抓取日期
    date = models.DateTimeField(auto_now_add=True)
    #是否被所有的账号转发过
    is_done = models.BooleanField(default=False)

class TransmitedRelationship(models.Model):
    #账号
    bot_id = models.CharField(null=False,max_length=100)
    #微博
    weibo_id = models.CharField(null=False,max_length=100)


class ProxyRecord(models.Model):
    #代理ip
    proxy = models.CharField(null=False,max_length=100)

class SendContent(models.Model):
    #新闻内容
    content=models.TextField(primary_key=True,null=False,max_length=1000)

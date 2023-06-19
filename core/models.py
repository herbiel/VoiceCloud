from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.




class Domain(models.Model):
    domain = models.CharField(max_length=20,verbose_name="域名")
    enable = models.BooleanField(default=False,verbose_name=u"启用")
    class Meta:
        verbose_name = "域名"
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.domain


class UserProfile(AbstractUser):
    domain = models.CharField(max_length=200,verbose_name=u'域名',default="")
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.username

class Extension(models.Model):
    number = models.CharField(max_length=20,verbose_name=u"分机号码",default="")
    password = models.CharField(max_length=20,verbose_name=u"密码",default="")
    displayname = models.CharField(max_length=20,verbose_name=u"显示名字",default="")
    domain = models.CharField(max_length=20,verbose_name=u"域名",default="")
    enable = models.BooleanField(default=False,verbose_name=u"启用")
    class Meta:
        verbose_name = u"分机"
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.number


class Gateway(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"名称",default="")
    username = models.CharField(max_length=20, verbose_name=u"用户名",default="")
    password = models.CharField(max_length=20,verbose_name=u"密码",default="")
    realm = models.CharField(max_length=20,verbose_name=u"认证地址",default="")
    proxy = models.CharField(max_length=20,verbose_name=u"认证代理",default="")
    domain = models.CharField(max_length=20, verbose_name=u"域名",default="")
    register = models.BooleanField(default=False,verbose_name=u"是否注册")
    enable = models.BooleanField(default=False, verbose_name=u"启用")

    class Meta:
        verbose_name = u"网关"
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.name

class Dialplan(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"名称",default="")
    gateway = models.CharField(max_length=50, verbose_name=u"网关",default="")
    expression = models.TextField(max_length=20, verbose_name=u"匹配条件",default="")
    domain = models.CharField(max_length=20, verbose_name=u"域名",default="")
    enable = models.BooleanField(default=False, verbose_name=u"启用")

    class Meta:
        verbose_name = u"路由"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

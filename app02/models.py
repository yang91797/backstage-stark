from django.db import models

# Create your models here.


class Host(models.Model):
    """
    主机表
    """
    host = models.CharField(verbose_name='主机表', max_length=32)
    ip = models.GenericIPAddressField(verbose_name='IP')

    def __str__(self):
        return self.host


class Project(models.Model):
    """
    项目表
    """
    title = models.CharField(verbose_name='项目名称', max_length=32)


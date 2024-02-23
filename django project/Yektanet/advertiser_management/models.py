from urllib import request

from django.db import models
from datetime import datetime



class advetiser(models.Model):
    # Field Names
    name = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.name


class ad(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    link = models.CharField(max_length=200, default="")
    advertiser = models.ForeignKey(to=advetiser, on_delete=models.PROTECT)
    approve = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class click(models.Model):
    ad = models.ForeignKey(to=ad, on_delete=models.PROTECT)
    created_on = models.DateTimeField(default=datetime.now)
    user_ip = models.CharField(max_length=100)


class view(models.Model):
    ad = models.ForeignKey(to=ad, on_delete=models.PROTECT)
    created_on = models.DateTimeField(default=datetime.now)
    user_ip = models.CharField(max_length=100)

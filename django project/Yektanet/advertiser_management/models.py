from urllib import request

from django.db import models
from datetime import datetime


class advetiser(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class ad(models.Model):
    title = models.CharField(max_length=200, )
    image = models.ImageField(upload_to="images/%Y/%m/%d",
                              help_text="image of the ad should be added in this part.")
    link = models.CharField(max_length=200, default="")
    advertiser = models.ForeignKey(to=advetiser, on_delete=models.CASCADE, help_text="Advertiser who created this ad.")
    approve = models.BooleanField(default=False, help_text="Each ad must be approved by the admin before being shown.")

    def __str__(self) -> str:
        return self.title


class click(models.Model):
    ad = models.ForeignKey(to=ad, on_delete=models.CASCADE, help_text="What ad was clicked on.")
    created_on = models.DateTimeField(auto_now_add=True)
    user_ip = models.CharField(max_length=100)


class view(models.Model):
    ad = models.ForeignKey(to=ad, on_delete=models.CASCADE, help_text="What ad has been viewed.")
    created_on = models.DateTimeField(auto_now_add=True)
    user_ip = models.CharField(max_length=45)

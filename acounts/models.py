from django.urls import reverse
from django.db import models

class Website(models.Model):
    url = models.CharField(max_length=255,null=True,blank=True)

class Acounts(models.Model):
    phone = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255,null=True,blank=True)
    status = models.IntegerField()
    website = models.ForeignKey(Website,on_delete=models.CASCADE,null=False,blank=False)
    timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)
    class Meta:
        db_table = 'accounts'
        ordering = ["-timestamp"]


    def __str__(self):
        return self.phone


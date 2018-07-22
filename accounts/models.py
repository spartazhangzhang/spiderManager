from django.urls import reverse
from django.db import models
class Website(models.Model):
    name = models.CharField(max_length=255,default=None,null=False,blank=False)
    url = models.CharField(max_length=255,null=False,blank=False)

    class Meta:
        verbose_name_plural='网站'

    def __str__(self):
        return self.name

class Acounts(models.Model):
    phone = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255,null=True,blank=True)
    status = models.IntegerField(default=False,null=True,blank=True)
    cookie = models.TextField(default=None,null=True,blank=True)
    ip = models.CharField(max_length=125,null=True,blank=True)
    # website = models.CharField(max_length=255,null=False,blank=False)
    website = models.ForeignKey(Website,on_delete=models.CASCADE,null=False,blank=False)
    timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)
    class Meta:
        db_table = 'accounts'
        ordering = ["-timestamp"]
        verbose_name_plural='账号'

    def __str__(self):
        return self.phone

    def get_delete_url(self):
        return reverse('accounts:delete',kwargs={"phone":self.phone})

    def get_update_url(self):
        return reverse('accounts:udpate',kwargs={'phone':self.phone})

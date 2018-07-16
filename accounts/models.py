from django.urls import reverse
from django.db import models

class Acounts(models.Model):
    phone = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255,null=True,blank=True)
    status = models.IntegerField(default=False)
    cookie = models.TextField(default=None,null=True)
    website = models.CharField(max_length=255,null=False,blank=False)
    # website = models.ForeignKey(Website,on_delete=models.CASCADE,null=False,blank=False)
    timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)
    class Meta:
        db_table = 'accounts'
        ordering = ["-timestamp"]

    def __str__(self):
        return self.phone

    def get_delete_url(self):
        return reverse('accounts:delete',kwargs={"phone":self.phone})

    def get_update_url(self):
        return reverse('accounts:udpate',kwargs={'phone':self.phone})

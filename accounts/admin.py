from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from accounts.models import Acounts,Website

class AccountsAdmin(admin.ModelAdmin):
    list_display = ["phone", 'password','status','cookie','website','timestamp','ip']
    list_display_links = ["timestamp"]
    list_editable = ["ip"]
    search_fields = ["phone", 'website']

    class Meta:
        model = Acounts

class WebAdmin(admin.ModelAdmin):
    list_display = ['name','url']
    search_fields = ['name','url']
admin.site.register(Acounts,AccountsAdmin)
admin.site.register(Website,WebAdmin)
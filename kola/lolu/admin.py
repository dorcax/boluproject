from django.contrib import admin
from .models import product,Order,staff
#from django.contrib.auth.models import User
admin.site.site_header = 'Omololu Dashboard'


class productAdmin(admin.ModelAdmin):
    list_display=('name','quantity','category')
    list_filter  =['category']
   

# Register your models here.
admin.site.register(product,productAdmin)
admin.site.register(Order)
admin.site.register(staff)
#admin.site.register(Tag)
#admin.site.unregister(User)


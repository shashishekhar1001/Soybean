from django.contrib import admin
from .models import *
# Register your models here.
class SoybeanPurchaseAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'variety', 'quantity', 'purchase_date', 'total_payment', 'payment_done')

admin.site.register(SoybeanPurchase, SoybeanPurchaseAdmin)
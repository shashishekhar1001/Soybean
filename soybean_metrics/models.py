from django.db import models
# import datetime
from datetime import datetime

# Create your models here.
class SoybeanPurchase(models.Model):
    farmer_name            = models.CharField(max_length=50)
    purchase_date          = models.DateField(blank=True, null=True)
    moisture               = models.IntegerField(default=10)
    VARIETY = (
        ('726', 'KDS 726'),
        ('753', 'KDS 753'),
        ('1460', 'MACS 1460'),
        ('335', 'JS 335'),
    )
    variety                = models.CharField(max_length=15, choices=VARIETY)
    quantity               = models.IntegerField()
    price_per_unit         = models.IntegerField()
    total_payment          = models.BigIntegerField(blank=True, null=True)
    payment_done           = models.BooleanField()
    discount_percentage    = models.IntegerField(default=0)
    payment_details        = models.TextField(max_length=250)


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.purchase_date = self.purchase_date or datetime.now(UTC)
    #     self.total_payment = self.quantity * self.price_per_unit

    def save(self, *args, **kwargs):
        self.purchase_date = self.purchase_date or datetime.now()
        self.total_payment = self.quantity * self.price_per_unit
        super().save(*args, **kwargs)

    def __str__(self):
        return self.farmer_name 
from django.contrib import admin
from .models import PaymentGateway,Invoice,InvoiceDetails


# Register your models here.
class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display=["token","balance","expiry_date","is_active",]

    class Meta:
        model=PaymentGateway

admin.site.register(PaymentGateway,PaymentGatewayAdmin)
admin.site.register(InvoiceDetails)
admin.site.register(Invoice)
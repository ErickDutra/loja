from django.contrib import admin
from . import models
# Register your models here.

class ItemOrderInline(admin.TabularInline):
    model = models.ItemOrder
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inline = [
        ItemOrderInline
    ]


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.ItemOrder)


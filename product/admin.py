from django.contrib import admin
from . import models

class VariactionInline(admin.TabularInline):
    model = models.Variaction
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    inline = [
        VariactionInline
    ]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Variaction)

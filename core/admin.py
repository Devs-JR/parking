from django.contrib import admin
from .models import Pessoa, Vehicle, Brand, Parameters, MoveRotate



class MoveRotateAdmin(admin.ModelAdmin):
    list_display = (
        'checkin',
        'checkout',
        'value_per_hour',
        'vehicle',
        'paid',
        'total',
        'total_hour',
    )


# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Vehicle)
admin.site.register(Brand)
admin.site.register(Parameters)
admin.site.register(MoveRotate, MoveRotateAdmin)
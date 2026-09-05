from django.contrib import admin
from .models import Service, Booking 

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'service',
        'date',
        'time',
        'status',
    )

    list_filter = ('status', 'service', 'date')
admin.site.register(Service)
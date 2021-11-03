from django.contrib import admin
from .models import advisor
from booking.models import Booking
admin.site.register(advisor)
admin.site.register(Booking)


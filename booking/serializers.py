from rest_framework import serializers
from .models import Booking
class BookingSerializer(serializers.ModelSerializer):
    # blog = serializers.StringRelatedField()
    class Meta:
        model = Booking
        #fields = ['name', 'email', 'phone', 'bookedfor']
        fields = '__all__'


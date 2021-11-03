from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .serializers import BookingSerializer
from .models import Booking
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
#from user.models import User
from rest_framework import generics
class BookingCreateAPIView(generics.GenericAPIView):
    permission_classes= [IsAuthenticated]
    #orders = Booking.objects.get(user=request.user)
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    bookings = Booking.objects.order_by('created_at')

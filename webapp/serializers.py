from rest_framework import serializers
from .models import advisor
class advseri(serializers.ModelSerializer):
    class Meta:
        model=advisor
        #fields=('firstname','lastname')
        fields='__all__'
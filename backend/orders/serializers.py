from rest_framework import serializers
from .models import orders
class orderserilizer(serializers.ModelSerializer):
    class Meta:
        model=orders
        fields = ('id','product','customernum')
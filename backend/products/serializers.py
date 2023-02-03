from rest_framework import serializers
from .models import CreateProduct,createSellers
class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=CreateProduct
        fields = ('id','name','price','full_detail','images')
class sellerserializer(serializers.ModelSerializer):
    class Meta:
        model=createSellers
        fields=('id','fullname','adress','phonenum')
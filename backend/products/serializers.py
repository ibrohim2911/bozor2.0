from rest_framework import serializers
from .models import CreateProduct,createSellers
class Productserializer(serializers.ModelSerializer):
    sotuvchi = serializers.SerializerMethodField()
    class Meta:
        model=CreateProduct
        fields = ('id','name','price','full_detail','images','sotuvchi', 'producttype')
    def get_sotuvchi(self, obj):
        return obj.seller.fullname if obj.seller else ''
class sellerserializer(serializers.ModelSerializer):
    class Meta:
        model=createSellers
        fields=('id','fullname','adress','phonenum')
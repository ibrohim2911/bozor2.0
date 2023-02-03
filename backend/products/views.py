from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.http import HttpResponse



from .models import createSellers,CreateProduct
from .serializers import Productserializer,sellerserializer
# Create your views here.
class sellerview(ListAPIView):
    queryset = createSellers.objects.all()
    serializer_class = sellerserializer

class detailseller(RetrieveAPIView):
    queryset = createSellers.objects.all()
    serializer_class = sellerserializer
class productview(ListAPIView):
    queryset = CreateProduct.objects.all()
    serializer_class = Productserializer

class detailproduct(RetrieveAPIView):
    queryset = CreateProduct.objects.all()
    serializer_class = Productserializer
def msgsender(request):

    

    msg = """    all urls 
    sellers/
    sellers/[id]/
    product/
    product[id]/
    orders/
    orders/[id]/
    admin/

    admin login: 
    username: user
    password: 1
    """

    return HttpResponse(msg, content_type='text/plain')
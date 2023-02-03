from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import orders
from .serializers import orderserilizer
# Create your views here.
class listorders(ListAPIView):
    queryset = orders.objects.all()
    serializer_class = orderserilizer

class detailorder(RetrieveAPIView):
    queryset = orders.objects.all()
    serializer_class = orderserilizer

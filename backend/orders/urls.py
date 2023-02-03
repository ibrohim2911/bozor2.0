from django.urls import path
from .views import listorders,detailorder,createorderview

urlpatterns = [
    path('orders/<int:pk>/', detailorder.as_view()),
    path('orders/',listorders.as_view()),
    path('orders/send/',createorderview.as_view())
]

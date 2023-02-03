from django.urls import path
from .views import detailproduct,detailseller,productview,sellerview,msgsender

urlpatterns = [
    path('product/<int:pk>/', detailproduct.as_view()),
    path('product/',productview.as_view()),
    path('sellers/<int:pk>/', detailseller.as_view()),
    path('sellers/',sellerview.as_view()),
    path('',msgsender,name='main')
]

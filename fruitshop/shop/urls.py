from django.urls import path
from .views import ProductView,shop

urlpatterns = [
    path('',ProductView.as_view(),name='home'),
    path('shop/',shop.as_view(),name='shop'),
]


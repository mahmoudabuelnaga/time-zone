from django.urls import path
from .views import HomeView, ShopView, ProductDetailView

app_name = 'product'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<int:pk>/<slug>/',
         ProductDetailView.as_view(), name='product_detail'),
]

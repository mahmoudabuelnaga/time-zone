from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Product, Image, Like
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from .forms import LikeForm
# Create your views here.


class HomeView(View):
    def get(self, *args, **kwargs):
        new_arrivals = Product.objects.filter(newest=True)[:3]
        popular_items = Product.objects.filter(most_populer=True)
        # form = LikeForm()

        context = {
            'new_arrivals': new_arrivals,
            'popular_items': popular_items,
            # 'form': form,
        }
        return render(self.request, 'product/index.html', context)


class ShopView(View):
    def get(self, *args, **kwargs):
        newest_arrivals = Product.objects.filter(newest=True)
        price_high_to_low = Product.objects.order_by('-price',)
        most_populer = Product.objects.filter(most_populer=True)

        page = self.request.GET.get('page', 1)
        paginator = Paginator(price_high_to_low, 18)

        try:
            price_high_to_low = paginator.page(page)

        except PageNotAnInteger:
            price_high_to_low = paginator.page(1)

        except EmptyPage:
            price_high_to_low = paginator.page(paginator.num_pages)

        context = {
            'newest_arrivals': newest_arrivals,
            'price_high_to_low': price_high_to_low,
            'most_populer': most_populer,
        }

        return render(self.request, 'product/shop.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_details.html'
    context_object_name = 'product'

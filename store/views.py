from django.urls.converters import SlugConverter
from category.models import category
from django.shortcuts import get_object_or_404, render
from .models import Product
# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_avaliable=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_avaliable=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)
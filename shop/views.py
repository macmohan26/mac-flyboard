from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.temp import CartAddProductForm
from django.contrib.auth.decorators import login_required

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    #products = products.filter(category=category)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/Products/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})
@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/Products/detail.html',
                  {'product': product,'cart_product_form': cart_product_form})
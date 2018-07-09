from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    drinks = Category.objects.filter(name="Drinks")
    drink_prod = Product.objects.all().filter(category=drinks)[:4]
  
    vegetables = Category.objects.filter(name="vegetables")
    veg_prod = Product.objects.all().filter(category=vegetables)[:4]
   
    fruits = Category.objects.filter(name="fruit")
    fru_prod = Product.objects.all().filter(category=fruits)[:4]
    print fruits
    category = None
    categories = Category.objects.all()
    product = Product.objects.all()[:4]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': product,
        'drink':drink_prod,
        'veg':veg_prod,
        'fruit':fru_prod,

    }
    return render(request, "newbase.html", context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product':product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'product/product_detail2.html', context)



def category_detail(request, id):
    category = Category.objects.get(id=id)
    prod =  Product.objects.all().filter(category=category)
    print prod
    context = {
        'post':category,
        'prod':prod,
    }
    return render(request, 'category/detail.html', context)

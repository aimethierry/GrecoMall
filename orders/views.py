from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Order, OrderItem
from product.models import Product
from cart.cart import Cart
from .forms import OrderCreateForm


# Create your views here.
def allorder(request, id):
    post = get_object_or_404(Product, id=id)
    # product = Product.objects.all()
    # name = OrderItem.objects.all().filter(product=product)
    context = {
        "post" : post 
    }

    return render(request, "order/all.html", context)


def order_create(request):
    cart = Cart(request)
   
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return HttpResponse("done in a good way ")
    else:
        form = OrderCreateForm()
    return render(request, 'order/order2.html', {'form': form, 'item':cart })
        
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from product.models import Product, Category
from orders.models import Order, OrderItem
from .forms import CategoryForm, ProductForm

def home(request):
    return render(request, 'dashboard/dashboard.html')

def category_create(request):
    form = CategoryForm(request.POST, request.FILES )
    if request.method =='POST':
        form = CategoryForm(request.POST, request.FILES )
        if form.is_valid():
            instance = form.save()
            instance.save()
            print "succeed"
            return redirect('/dashboard/create_category/')
    else:
        context = {
            'form':form
        }
    return render(request, 'dashboard/category_create.html',{'form': form} )



def product_create(request):
    form = ProductForm(request.POST, request.FILES )
    if request.method =="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.save()
            print "succeed"
            return redirect('/dashboard/product_create/')
    else:
        context = {
            'form':form
        }
    return render(request, 'dashboard/product_create.html', {'form': form })


def all_order(request):
    name = Order.objects.all()
    print name
    context = {
        'object_list': name
    }
    return render(request, 'dashboard/all_order.html', context)


def order_detail(request, id=None):
    name = get_object_or_404(Order, id=id)
    data = OrderItem.objects.all().filter(order=name)
    print data 
    context = {
        'detail':name,
        'item': data
    }
    return render(request, "dashboard/detail.html", context)





def all_product(request):
    name = Product.objects.all()
    context = {
        'product':name
    }
    return render(request, "dashboard/all_product.html", context)



def product_edit(request, id=None):
    ok = Product.objects.get(id=id)
    print ok
    form = ProductForm(request.POST, request.FILES)
    if request.method =="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.save()
            print "succeed"
            return redirect('/dashboard/product_create/')

    else:
        context = {
            'instance':ok,
            'form':form
        }
    return render(request,"dashboard/product_edit.html", {'instance':ok, 'form':form})
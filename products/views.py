from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    category = Product.objects.order_by('priority')[:4]
    latest = Product.objects.order_by('id')[:3]
    return render(request,'index.html',{'category':category,'latest':latest})

def pro(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    category = Product.objects.order_by('priority')
    product_paginator=Paginator(category,2)
    category=product_paginator.get_page(page)
    return render(request,'products.html',{"category": category})

def product_details(request,id):
    obj = Product.objects.get(id=id)
    return render(request,'product_details.html',{'obj':obj})
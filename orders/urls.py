from django.urls import path
from .import views

urlpatterns =[
    path('cart/',views.cart,name="cart"),
    path('orders/',views.cart_orders,name="orders"),

    path('add_to_cart/',views.add_to_cart,name="add_to_cart"),
    path('remove/<id>/',views.remove_item,name='del'),
    path('check/',views.checkout_cart,name='check'),
  
]
from django.urls import path
from .import views

urlpatterns =[
    path('',views.index,name='ind'),
    path('pro/',views.pro,name='pro'),
    path('pro_details/<id>',views.product_details,name='pro_details'),
]
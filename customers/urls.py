from django.urls import path
from .import views

urlpatterns = [
    path('account/',views.show_account,name='account'),
    # path('log',views.loginn,name='log'),
    path('logout',views.logouts,name='logout'),

]



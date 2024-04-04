from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    
    path('',views.payment_opt,name='payment_opt'),
    path('success',views.pay_success,name='success'),
    path('order',views.order,name='order'),
]
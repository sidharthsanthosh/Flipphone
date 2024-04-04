
from django.urls import path
from.import views

app_name='flipphoneapp'

urlpatterns = [
    path('',views.index),
    path('register',views.register,name='register'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('cart',views.cart,name='cart'),
    path('logout',views.logout,name='logout'),
    path('product' ,views.product,name='product'),
    path('brand/' ,views.brand,name='brand'),
    path('search/' ,views.search,name='search'),
    path('view_product/' ,views.view_product,name='view_product'),
    path('search/view_product/' ,views.view_product,name='view_product'),
    path('apple',views.apple,name='apple'),
    path('samsung/',views.samsung,name='samsung'),
    path('xiaomi',views.xiaomi,name='xiaomi'),
    path('google',views.google,name='google'),
    path('realme',views.realme,name='realme'),
    path('poco',views.poco,name='poco'),
    
]
   
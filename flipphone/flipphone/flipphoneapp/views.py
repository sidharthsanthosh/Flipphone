from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate
from django.contrib.auth.models import User
from .models import register_table,product_tbl

from.models import register_table
from django.db.models import Q

# Create your views here.
def index(request):
    obj = product_tbl.objects.all()
    obj = obj[:6]
    return render(request,'index.html',{"data":obj})


def view_product(request):
    idn  = request.GET['idn']
    obj = product_tbl.objects.filter(id=idn)
    # obj2 = Direct_buy.objects.all()
    # obj2.delete()
    return render(request,"product_details.html",{"data":obj})

def login(request):
    return render(request,'login.html')

def cart(request):
    return render(request,'cart.html')


def brand(request):
    return render(request,'brand.html')

def register(request):
    if request.method=="POST":
        nam1=request.POST.get('name')
        em1=request.POST.get('email')
        pas1=request.POST.get('password')
        try:
            user=User.objects.create_user(first_name=nam1,username=em1,password=pas1)
            return redirect("/")
        except Exception as e:
            error = str(e)
         # obj=register_table.objects.create(nam=nam1,eml=em1,pas=pas1)
        # print(nam1)
        # print(em1)
        # if obj:
        #     return render(request,"index.html")
        # else:
            return render(request,"login.html")
    # else:
        return render(request,"login.html")
def login(request):
    if request.method=="POST":
        em2=request.POST.get('email1')
        pass2=request.POST.get('password1')
        # obj=register_table.object.filter(eml=em2,pas=pass2)
        user=authenticate(username=em2,password=pass2)
    
        if user:
        #     request.session['email']=em2
        #     request.session['password']=pass2
        #     for ls in obj:
        #         idno=ls.id
        #         request.session['idn']=idno
        #     return render(request,'index.html')
        # else:
        #     request.session['email']=''
        #     request.session['password']=''
        #     msg='invaild email or password'
        #     return render(request,'login.html',{'error':msg})
            authlogin(request,user)
            return redirect("/",{"user":user})
        
        else:
            messages.info(request,"Invaild message or password")
            return redirect("/login")
    return render(request,'login.html')  
def logout(request):
    authlogout(request)
    return redirect('/')
     
def product(request):
    obj=product_tbl.objects.all()
    if obj:
        return render(request,'product.html',{"data":obj})
    return render(request,'product.html')

def search(request):
    query=None

    if "keyword" in request.GET:
        query=request.GET.get('keyword')
        products=product_tbl.objects.all().filter(Q(product_name__contains=query) | Q(product_price__contains=query))
        return render(request,'search.html',{'query':query,'data':products})
    
def apple(request):
    obj = product_tbl.objects.filter(c_name__iexact='apple')
    return render(request,"brand_icon.html",{"data":obj})

def samsung(request):
    obj = product_tbl.objects.filter(c_name__iexact='samsung')
    return render(request,"brand_icon.html",{"data":obj})


def xiaomi(request):
    obj = product_tbl.objects.filter(c_name__iexact='xiaomi')
    return render(request,"brand_icon.html",{"data":obj})


def poco(request):
    obj = product_tbl.objects.filter(c_name__iexact='Poco')
    return render(request,"brand_icon.html",{"data":obj})


def google(request):
    obj = product_tbl.objects.filter(c_name__iexact='google')
    return render(request,"brand_icon.html",{"data":obj})


def realme(request):
    obj = product_tbl.objects.filter(c_name__iexact='realme')
    return render(request,"brand_icon.html",{"data":obj})
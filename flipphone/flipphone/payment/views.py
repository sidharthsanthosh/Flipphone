from django.shortcuts import render,redirect
from cart.models import CartItem,Direct_buy
import uuid
from . models import Payment_details
from datetime import date
# Create your views here.


# --------- date generation ---------
today = date.today()
order_date = date.today()
if today.day < 23:
       
    new_date  = str(today.day + 5)
    odm = str(today.month)
    ody = str(today.year)
    delivery_date = ody + "-" + odm + "-" + new_date
      
else:
    if today.month == 12:
        new_year = today.year + 1
        new_date = 5
        new_month = 1
        odt = str(new_date)
        odm = str(new_month)
        ody = str(new_year)
        delivery_date = ody + "-" + odm + "-" + odt
          
    else:   
        new_date = 1
        new_month = today.month + 1
        odt = str(new_date)
        odm = str(new_month)
        ody = str(today.year)
        delivery_date = ody + "-" + odm + "-" + odt 


# --------- payment section -------------

def payment_opt(request):
    p = request.META.get('HTTP_REFERER')
    delivery_date = "your_delivery_date"
    if p == "http://127.0.0.1:8000/cart/buy_detail":
        obj = Direct_buy.objects.all()
        totals = []
        pro_quant = {}
        for i in obj:  
            totals.append(i.total) 
            pro_quant[i.product.product_name]=i.quantity   
              

        data = {"total":totals[-1] if totals else 0, "items":pro_quant,"del_date":delivery_date,"path":"direct"}
        return render(request,'payment.html',data)
    else:
        obj = CartItem.objects.all()
        totals = []
        pro_quant = {}
        for i in obj:  
            totals.append(i.total)  
            pro_quant[i.product.product_name]=i.quantity  
        
        data = {"total":totals[-1] if totals else 0, "items":pro_quant,"del_date":delivery_date,"path":"cart"}
        return render(request,'payment.html',data)




def pay_success(request):
    if request.method == "POST":
        add = request.POST.get('addr')
        mb = request.POST.get('mob')
        pin = request.POST.get('pn')
        meth = request.POST.get('tab')
        p = request.POST.get('path')

    if p == "direct":
        obj = Direct_buy.objects.all()
        totals = []
        pro_quant = {}
        for i in obj:
            totals.append(i.total)
            print("b total ",totals)
            pro_quant[i.product.product_name] = i.quantity

        total = totals[-1] if totals else 0  # Check if totals is empty
    else:
        obj = CartItem.objects.all()
        totals = []
        pro_quant = {}
        for i in obj:
            totals.append(i.total)
            pro_quant[i.product.product_name] = i.quantity

        total = totals[-1] if totals else 0  # Check if totals is empty

    users = request.user
    user = users.first_name
    unique_id = str(uuid.uuid4())

    if request.method == "POST":
        add = request.POST.get('addr')
        mb = request.POST.get('mob')
        pin = request.POST.get('pn')
        meth = request.POST.get('tab')
        orders = Payment_details.objects.create(
            user=user,
            address=add,
            mobile=mb,
            Pin=pin,
            products=pro_quant,
            amount=total,
            pay_method=meth,
            order_id=unique_id,
            o_date=order_date,  # Assuming order_date is defined somewhere in your code
            d_date=delivery_date  # Assuming delivery_date is defined somewhere in your code
        )
        orders.save()

        obj.delete()
        return render(request, 'success.html', {'trans_id': unique_id})
    else:
        return render(request, 'error.html', {'message': 'Invalid request method'})


# -------- view orders ------

def order(request):
    users = request.user
    # valid = ""
    flag = 1
    first_name = users.first_name

    orders = Payment_details.objects.filter(user=first_name)

    # print("today type ",type(today.day))
    # li = ""
    # for i in orders:
    #         li = i.d_date
            
    

    # print("list ",li)
    
    # print("last",li[-1])
    # print("scnd",li[-2])

    # if li[-2] != "-":
    #         dd_date = int(str(li[-2]) + str(li[-1]))
    #         print("hello")
    #         print(type(li[-2]))
    # else:
    #     dd_date = int(li[-1])

    # print(" -2 --- ",(li[-2]))
    # print(" -1 --- ",(li[-1]))
    # print("ddd ",dd_date)



    # if dd_date == today.day:
    #     msg = "Delivery today"
    #     flag = 2
        
    #     print("dt ",dd_date, "td ", today.day )
    # elif dd_date > today.day:
    #      flag = 3
    #      msg = "delivered"
            
    return render(request,"order.html",{"data":orders,"flag":flag})

  

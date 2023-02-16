from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

from django.http import HttpResponse
from .forms import *


#create your views here.
def login(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save() 
         
            username = request.POST.get('username')
            password = request.POST.get('password')
            u1="Nagalakshmi"
            p1="n123i"
            u2="Manager"
            p2="m123r"
            
            if username==u1 and password==p1 :  
                return redirect ('home')
            if username==u2 and password==p2 :
                return redirect ('home2')
            else: 
                
                messages.error(request,'login failed')
                return redirect('login')
        
        else: 
            return render(request,'login.html')
    else:
        form = LoginForm()        
    context = {
        'form': form
    }
        
    return render(request, 'login.html', context)

def home(request):
    mydata=Store_product.objects.all()
    if(mydata!=''):
        return render(request,'product/product.html',{'datas':mydata})
    else:
        return render(request,'product/product.html')
        
def addData(request):
    if request.method=="POST":
        product_name=request.POST.get('product_name')
        quantity=request.POST.get('quantity')
        amount=request.POST.get('amount') 
        delivered=request.POST.get('delivered')
        remaining=request.POST.get('remaining')
        
        Store_product.objects.create(
          product_name=product_name,
          quantity=quantity,
          amount=amount,
          delivered=delivered,
          remaining=remaining)
        messages.success(request,'New product Created!')  
        return redirect('home')
    return render(request,'product/product.html')

def updateData(request,id):
    mydata=Store_product.objects.get(id=id)
    if request.method=="POST":
        product_name=request.POST.get('product_name')
        quantity=request.POST.get('quantity')
        amount=request.POST.get('amount') 
        delivered=request.POST.get('delivered')
        remaining=request.POST.get('remaining')
        
        mydata.product_name=product_name
        mydata.quantity=quantity
        mydata.amount=amount
        mydata.delivered=delivered
        mydata.remaining=remaining
        mydata.save()
        messages.success(request,' Updated successfully!') 
        return redirect('home')

    return render(request,'product/update.html',{'data':mydata})

def deleteData(request,id):
    mydata=Store_product.objects.get(id=id)
    mydata.delete()
    messages.success(request,'product deleted') 
    return redirect('home')

def home2(request):
    mydata=Store_employee.objects.all()
    if(mydata!=''):
        return render(request,'manager.html',{'datas':mydata})
    else:
        return render(request,'manager.html')
        
def addData2(request):
    if request.method=="POST":
        employee_name=request.POST.get('employee_name')
        email=request.POST.get('email')
        address=request.POST.get('address') 
        contactno=request.POST.get('contactno')
        salary=request.POST.get('salary')
        
        Store_employee.objects.create(
          employee_name=employee_name,
          email=email,
          address=address,
          contactno=contactno,
          salary=salary)
        messages.success(request,'New Employee Created!')  
        return redirect('home2')
    return render(request,'manager.html')

def updateData2(request,id):
    mydata=Store_employee.objects.get(id=id)
    if request.method=="POST":
        employee_name=request.POST.get('employee_name')
        email=request.POST.get('email')
        address=request.POST.get('address') 
        contactno=request.POST.get('contactno')
        salary=request.POST.get('salary')
        
        mydata.employee_name=employee_name
        mydata.email=email
        mydata.address=address
        mydata.contactno=contactno
        mydata.salary=salary
        mydata.save()
        messages.success(request,' Updated successfully!') 
        return redirect('home2')

    return render(request,'update.html',{'data':mydata})

def deleteData2(request,id):
    mydata=Store_employee.objects.get(id=id)
    mydata.delete()
    messages.success(request,'Employee Deleted') 
    return redirect('home2')

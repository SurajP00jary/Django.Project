from django.core.mail import EmailMessage

import os
from random import randint
from django import forms
from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime
from hello.models import Customer, Hello, Products, farmer, plant, seeds,Order
from django.core.mail import send_mail
from django.http import HttpResponse
import hashlib
from xhtml2pdf import pisa
import random

# Create your views here.
def signup(request):
    return render(request,'signup.html')

def usignup(request):
  uname=request.GET.get('usrname')
  pwds=request.GET.get('pswd')
  pwds=hashlib.md5(pwds.encode('utf-8')).hexdigest()
  mobilenumbers=request.GET.get('mobilenumber')
  emailids=request.GET.get('emailid')
  addressd=request.GET.get('address')
  pincodes=request.GET.get('pincode')
  print(uname,mobilenumbers,emailids,pwds,addressd,pincodes)
  try:
      g=Customer.objects.get(emailid=emailids)
      if g is not None:
          return HttpResponse("Email Already exists")
  except:

       u=Customer(username=uname,mobilenumber=mobilenumbers,emailid=emailids,pwd=pwds,address=addressd,pincode=pincodes)
       u.save()
       u=Customer.objects.get(emailid=emailids)
       res = send_mail("Regsitration", "Congratulations!.Welcome To The Family of SSSV..! Your registration is successfull and your customer id is "+str(u.id), "sssvnursery@gmail.com", [emailids])
       return render(request,'login.html')
def greet(request):
 dt=datetime.datetime.now()
 name="Chetan"
 subjects=["PYT","CN","ATC"]
 return render(request,"dt.html",{"dt":dt,"name":name,"subjects":subjects})
def Nursery(request):
    return render(request,"Nursery.html")
def about(request):
    return render(request,"about.html")
    
def login(request):
    return render(request,"login.html")

def ulogin(request):
  uname=request.GET.get('usrname')
  pwds=request.GET.get('psw')
  pwds=hashlib.md5(pwds.encode('utf-8')).hexdigest()
  u=Customer.objects.filter(username=uname,pwd=pwds)
  
  if(u):
    response=render(request,"Nursery.html")
    response.set_cookie('usrname',uname)
    return response

  else:
      return render(request,"login.html")

def products(request):
    return render(request,"products.html")

def order(request):
     return render(request,"products.html")
def products(request):
    product_list=Products.objects.all()
    istr='''
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script>
    function ord(ono)
    {
        $.get("http://localhost:8000/uorder",{ono:ono}).done(function(data)
        {
            alert(data);
        
        });
    }
    </script>
       <header>
        <div class="navbar">
    <a href="/Nursery" class="navbar-brand">Home</a>
    <a href="/about" class="navbar-item">About</a>
    <a href="/products" class="navbar-item">Our Products</a>
    <a href="/search" class="navbar-item">Search</a>
    <a href="/adminlogin" class="navbar-item">Admin Login</a>

     </header>
    '''
    cnt=1
    for product in product_list:
        istr+='''
        <body>
     

        <div class="about-img">
                    <div id="about" class="about">

     
      <img src="http://localhost:8000/static/images/'''+str(cnt)+'''.jpg" alt="Sandwich" width="400px" height="300px">

            <h1>
          '''+product.product_name+'''</h1>
            <h2>Product Type:'''+product.product_type+'''</h2>
            <h2>Product Price:'''+str(product.product_price)+'''</h2>
                        <h2>Soil Type:'''+product.soil_type+'''</h2>
                        <h2>Botanical Name:'''+product.product_botname+'''</h2>
          <button style="color:Blue" type="button" class="btn btn-success" id="ordnow" onclick=ord('''+str(product.product_id)+''')> Order Now </button>
 
        </div>
            </div>
               </div>
               </div>
               </body>
                   <style>
                   
.navbar {
    
  display: flex;
  justify-content: space-around;
    background-color: rgb(2, 13, 17);
    font-size: 23px;
    font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    color: #ffffff;
    padding: 25px;  
    font-stretch: expanded;
}
.navbar a {
    text-decoration: none;
    color: inherit;
}
.navbar :hover{
    background-color: rgb(88, 84, 86);
    width: auto;
    padding:auto;
    height: auto;
    
    border-radius: 20px;
    
    
}

.navbar-brand {
    font-size: 1.2em;
    font-weight: 600;
}

.navbar-item {
    font-variant: small-caps;
   
}


footer{
    background-color: rgb(2, 13, 17);
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 20px;
    color:white;
    padding: 2px; 
}
h3{
    color: rebeccapurple;
}
                       body{
    background-color: rgb(243, 240, 208);
}
#res{
    padding-bottom: 0px;
    margin-top: 0px;
}
.about{
    column-count: 2;
    padding-top: 50px;
    padding-left: 50px;
    padding-bottom: 50px;
    padding-right: 50px;
}


 h1{
    color:rgb(238, 37, 121);
    font-weight: bolder;
    font-size: 30px;
} 
h4{
    font-size: solid black;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-weight: bold;
    font-size: 25px;
}

section::after {
    content: "";
    display: table;
    clear: both;
  }
  #about{
    background-color: hsl(143, 35%, 93%);
      margin: 0px;
      padding-top: 40px;
  padding-left: 100px;
  border-bottom:rgb(72, 179, 46) solid 10px;
  padding-bottom: 40px;
    }
button{
    color:rgb(35, 69, 161);
    background-color: rgb(160, 219, 148);
    height: 60px;
    width: 200px;
    font-size: 20px;
}


    h5{
  padding-left: 500px;
    font-size: 4rem;
    color: blue;
    }
    h6{    padding-left: 150px;
        padding-right: 130px;
        padding-top: 0px;
        color: rgb(9, 10, 10);
        font-family:inherit;
        font-size: 30px;
    }
    #hello{
        color: rgb(233, 203, 203);
        background-color: rgb(15, 78, 59);
    }

    </style>
    <script>
    function myFunction(){
      alert('Booking Confirmed!!!!...');

    document.getElementById('hello').innerHTML='Booked'
    window.location='/orderconf'
    }

      
    
    
  </script>
  
 ''' 
        cnt+=1
        if cnt%4==0:
         istr+='''''</div><div class="w3-row-padding w3-padding-16 w3-center">''''' ;
     
     
    return HttpResponse(istr)
def uorder(request): 
  uname=request.COOKIES.get('usrname')
  onos=request.GET.get('ono')
  f=Products.objects.get(product_id=onos)
  print(uname)
  print(f)
  print(onos)
  o=Order(customername=uname,Date=datetime.date.today(),product_id=onos,productname=f)
  o.save()
#   c=Customer.objects.get(username=uname)
#   email=c.emailid
#   m=Products.objects.get(product_id=onos)
#   mname=m.product_name
#   template = 'orderdetail.html'
#   context = {'ono' : onos,'product_name':mname,'uname':uname}
#   pdf = render_to_pdf(template, context)
#   email = EmailMessage("Order", "Products Booking", "sssv2021@gmail.com", [email])
#   email.content_subtype = "pdf"
#   email.attach('Products_Booking', pdf, 'application/pdf')
#   res = email.send()


  
  return HttpResponse('''Order Confirmed''')

        

def signup(request):
    return render(request,"signup.html")

# def orders(request):
#     return render(request,"orders.html")

def search(request):
    return render(request,"search.html")

def msearch(request):
    productnames=request.GET.get("productname")
    productlist=Products.objects.filter(product_name__icontains=productnames)
    str='''

    <br><br>
    <h2>Matched collections<h2/> 
    
     <style>
     h2 {
         color:black;
     }
     body{background-color:white}
.customers tr, .customers tr {
  border: 1px solid #ddd;
  padding: 8px;
}

.customers tr:nth-child(even){background-color: #f2f2f2;}

.customers tr:hover {background-color: #ddd;}

.table th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
.table{
    width:100%;
}
</style>
  
<table class="table">
            
                <tr class="w3-blue">
                    <th class="i">Product Name</th>
                    <th class="i">Product Type</th>
                     <th class="i">Soil Type</th>
                    </tr>
                    

''' 
    for product in productlist:
     str+="<tr><td>"+product.product_name+"</td><td>"+product.product_type+"</td><td>"+product.product_name+"<tr><td>";
    return HttpResponse(str) 

def search(request):
    return render(request,'search.html')
def orderconf(request):
 return render(request,'orderconf.html')
def stafflog(request):
 return render(request,'stafflog.html')

def stafflog(request):
    customers=Customer.objects.all()
    istr='''
    <h1>Customer Details</h1>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script>
    function ord(ono)
    {
        $.get("http://localhost:8000/ustafflog",{ono:ono}).done(function(data)
        {
            alert(data);
            $("body").html(data)
        });
    }
    </script>
    
       <style>
     h2 {
         color:blue;
     }
     h1 {text-align:center;
     background-color:violet;
         color:blue;
     }
     body{background-color:white;}
.customers tr, .customers tr {
  border: 1px solid #ddd;
  padding: 20px;
}

.customers tr:nth-child(even){background-color: #f2f2f2;}

.customers tr:hover {background-color: #ddd;}

.table th {
  padding-top: 0px;
  padding-bottom: 12px;
  text-align: left;
  background-color:red;
  color: white;
}
.table{
    font-size:25px;
    font-family:Times New Roman;
    width:100%;
    background-color:pink
    
    
}
</style>

    <table class="table">
             <tr class="w3-blue">
                    <th class="i">Customer Name</th>
                    <th class="i">Email ID</th>
                     <th class="i">Address</th>
                    <th class="i">Mobile Number</th>

                    </tr>

    '''
    cnt=1
    for customer in customers:
     istr+="<tr><td>"+customer.username+"</td><td>"+customer.emailid+"</td><td>"+customer.address+"</td><td>"+str(customer.mobilenumber)+"</td><tr>";   
    
    return HttpResponse(istr)
def hel(request):
    return render(request,"hel.html")
def adminlogin(request):
    return render(request,"adminlogin.html")
def uadminlogin(request):
    usname=request.GET.get("ussrname")
    pswrd=request.GET.get("psssw")
    if(usname=="sssv" and pswrd=="2021"):
      return render(request,"hel.html")
def sendSimpleEmail(request):
    res = send_mail("hi", "Hope you are doing fine", "sssvnursery@gmail.com", ["skr61471@gmail.com"])
    return HttpResponse('%s'%res)
def ordersrcv(request):
    return render(request,"ordersrcv.html")
def ordersrcv(request):
    orderss=Order.objects.all()
    istr='''
    <h1>Orders  Details</h1>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script>
    function ord(ono)
    {
        $.get("http://localhost:8000/uordersrcv",{ono:ono}).done(function(data)
        {
            alert(data);
            $("body").html(data)
        });
    }
    </script>
    
       <style>
     h2 {
         color:blue;
     }
     h1 {text-align:center;
     font-size:40px;
     background-color:rgb(80,80,80);
     padding-bottom:30px;
         color:black;
     }
     body{background-color:white;}
.customers tr, .customers tr {
  border: 1px solid #ddd;
  padding: 20px;
}

.customers tr:nth-child(even){background-color: #f2f2f2;}

.customers tr:hover {background-color: #ddd;}

.table th {
  padding-top: 10px;
  padding-bottom: 12px;
  text-align:center;
  background-color:rgb(104,0,0);
  color: white;
}
.table{
    font-size:25px;
    font-family:Times New Roman;
    width:100%;
    background-color:rgb(255, 230, 230);
    
    
}
</style>

    <table class="table">
             <tr class="w3-blue">
                    <th class="i">Customer Name</th>
                    <th class="i">Product ID</th>
                    <th class="i">Product Name</th>
                     <th class="i">Date of Order</th>

                    </tr>

    '''
    cnt=1
    for custo in orderss:
     istr+="<tr><td>"+str(custo.customername)+"</td><td>"+str(custo.product_id)+"</td><td>"+custo.productname+"</td><td>"+str(custo.Date)+"</td><tr>";   
    
    return HttpResponse(istr)

def getotp(request):
    otp = random.randint(000000,999999) 
    email=request.GET.get('email') 
    file_exists = os.path.exists('enm.txt')
    ss=''
    if file_exists:
       f = open("enm.txt", "r")
       for fh in f:
          s=fh.split(":")
          em=s[0]
          if em==email:
              continue
          s+=fh
       f.close()
    f = open("enm.txt", "w")
    ss+=email+":"+str(otp)
    f.write(ss)
    f.close()
    send_mail("OTP", "Your OTP is  "+str(otp), "sssv2021@gmail.com", [email])
    return HttpResponse('Mail sent')

#Get change of password html page
def cpass(request):
   return render(request,"cpass.html")

#implementing change of password method
def changepass(request):
    email=request.GET.get('email') 
    rotp=request.GET.get('rotp') 
    npsw=request.GET.get('npsw') 
    f = open("enm.txt", "r")
    for fh in f:
        s=fh.split(":")
        em=s[0]
        otp=s[1]
        if em==email and otp==rotp :
               c=Customer.objects.get(emailid=email)
               npsw=hashlib.md5(npsw.encode('utf-8')).hexdigest()
               c.pwd=npsw
               c.save()

               return HttpResponse("Password changed successfully")
    return HttpResponse("OTP invalid")
        


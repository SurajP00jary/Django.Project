from django.contrib import admin
from django.urls import path

from hello.views import greet,Nursery,about,login,signup,usignup,ulogin,msearch,search,products,orderconf,stafflog,adminlogin,uadminlogin,hel,sendSimpleEmail,ordersrcv,uorder,order,getotp,cpass,changepass
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [

path('admin/', admin.site.urls),
path('',login),
path('greet/',greet),
path('Nursery/',Nursery),
path('about/',about),
path('login/',login),
path('hel/',hel),
path('ulogin/',ulogin),
path('order/',order),
path('products/',products),
path('uorder/',uorder),
path('stafflog/',stafflog),
path('signup/',signup),
path('usignup/',usignup),
path('search/',search),
path('msearch/',msearch),
path('uadminlogin',uadminlogin),
path('orderconf/',orderconf),
path('adminlogin/',adminlogin),
path('ordersrcv/',ordersrcv),
path('SM/',sendSimpleEmail),
path('getotp/',getotp),
path('cpass/',cpass),
path('changepass/',changepass),







]
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 


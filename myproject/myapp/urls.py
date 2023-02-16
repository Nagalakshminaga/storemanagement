from django.urls import path

from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('home',views.home,name='home'),
    path('addData',views.addData,name='addData'),
    path('updateData/<int:id>',views.updateData,name='updateData'), 
    path('deleteData/<int:id>',views.deleteData,name='deleteData'),  
    path('home2',views.home2,name='home2'),
    path('addData2',views.addData2,name='addData2'),
    path('updateData2/<int:id>',views.updateData2,name='updateData2'), 
    path('deleteData2/<int:id>',views.deleteData2,name='deleteData2'), 
]
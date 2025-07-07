from django.urls import path

from . import views

urlpatterns = [

    path('register-as-business-man',views.register_as_business_man,name='register_as_business_man'),
    path('register-as-customer', views.register_as_customer, name='register_as_customer'),
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('base',views.base,name='base'),

    path('business-man-list',views.business_man_list,name='business_man_list'),
    path('update-business-man/<str:id>',views.update_business_man,name='update_business_man'),
    path('delete-business-man/<str:id>', views.delete_business_man, name='delete_business_man'),

    path('customer-list',views.customer_list,name='customer_list'),
    path('profile',views.profile,name='profile'),

]
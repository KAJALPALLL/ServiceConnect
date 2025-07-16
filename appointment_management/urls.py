from . import views
from django.urls import path

urlpatterns = [
    path('create-business-history',views.create_business_history,name='create_business_history'),
    path('book-appointment/<str:id>',views.book_appointment,name='book_appointment'),
    path('clients-appointment-list',views.clients_appointment_list,name='clients_appointment_list'),
    path('business-appointment-list',views.business_appointment_list,name='business_appointment_list'),
    path('appointment-list',views.appointment_list,name='appointment_list'),
    path('terms',views.terms,name='terms'),
    path('business-man-terms',views.business_man_terms,name='business_man_terms'),
    path('add-review/<str:id>',views.add_review, name='add_review'),
    path('add-conversation/<str:id>',views.add_conversation, name='add_conversation'),
    path('update-status/<str:id>', views.update_status, name='update_status'),
    path('appointment-status-update/<str:id>', views.appointment_status_update,name='appointment_status_update'),
    path('business-customer-list', views.business_customer_list, name='business_customer_list'),
    path('about-us', views.about_us, name='about_us'),
    path('business-man-about-us/<str:id>', views.business_man_about_us,name='business_man_about_us'),

]
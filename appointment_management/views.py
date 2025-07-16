from django.shortcuts import render,redirect
from . models import Business_History,BookAppointment, Reviews, Conversation, AboutUs
from datetime import timedelta,datetime
from user_management.models import user_profile



def create_business_history(request):
    if request.method == "POST":
        status = request.POST['status']
        business_data = Business_History.objects.create(business_man_id=request.user.id,start_datetime=datetime.now(),status=status)
        business_data.save()
        return redirect('customer_list')


def book_appointment(request,id):
    if request.method == "POST":
        datetime = request.POST['datetime']
        book_appointment = BookAppointment.objects.create(business_man_id=id,customer_id=request.user.id,datetime=datetime)
        book_appointment.save()
        return redirect('business_man_list')
    else:
        user_data = user_profile.objects.filter(id=id).first()
        return render(request,'book-appointment.html',{'data':user_data})


def clients_appointment_list(request):
    client_data = BookAppointment.objects.filter(customer_id=request.user.id)
    return render(request,'appointment-list.html',{'data':client_data})

def business_appointment_list(request):
    business_man_data = BookAppointment.objects.filter(business_man_id=request.user.id)
    return render(request, 'appointment-list.html', {'data': business_man_data})

def appointment_list(request):
    data = BookAppointment.objects.all()
    return render(request,'appointment-list.html',{'data':data})

def terms(request):
    return render(request,'terms.html')

def business_man_terms(request):
    return render(request,'business-man-terms.html')

def add_review(request,id):
    if request.method == "POST":
        description = request.POST['description']
        appointment_data = BookAppointment.objects.get(id=id)
        Reviews.objects.create(description=description, type="review", appointment_booking=appointment_data)
        return redirect('appointment_list')
    else:
        review_exist = Reviews.objects.filter(appointment_booking__id=id).first()
        if review_exist:
            return render(request,'add-review.html', {"id":id, "review_exist": review_exist})
        return render(request,'add-review.html', {"id":id})


def add_conversation(request,id):
    if request.method == "POST":
        description = request.POST['description']
        appointment_data = BookAppointment.objects.get(id=id)
        business_man_data = user_profile.objects.filter(groups__name="business_man", id=request.user.id).first()
        customer_data = user_profile.objects.filter(groups__name="customer", id=request.user.id).first()
        if business_man_data:
            Conversation.objects.create(description=description, appointment_booking=appointment_data, business_man=business_man_data)
        if customer_data:
            Conversation.objects.create(description=description, appointment_booking=appointment_data, customer=customer_data)
        
        return redirect('appointment_list')
    else:
        appointment_data = Conversation.objects.filter(appointment_booking_id=id)
        return render(request,'add-conversation.html', {"id": id, "appointment_data": appointment_data})



def update_status(request, id):
    if request.method == "POST":
        status = request.POST['status']
        appointment_data = BookAppointment.objects.filter(id=id).first()
        appointment_data.status = status
        appointment_data.save()
        return redirect('appointment_list')
    else:
        return redirect('appointment_list')



def appointment_status_update(request, id):
    if request.method == "POST":
        status = request.POST['status']
        appointment_data = BookAppointment.objects.filter(id=id).first()
        appointment_data.appointment_status = status
        appointment_data.save()
        return redirect('appointment_list')
    else:
        return redirect('appointment_list')



def business_customer_list(request):
    # Get all appointments for the logged-in business user
    appointment_list = BookAppointment.objects.filter(business_man=request.user)
    
    # Extract unique customer IDs from the appointments
    customer_ids = appointment_list.values_list('customer_id', flat=True).distinct()

    # Fetch customer data from UserProfile model
    users = user_profile.objects.filter(id__in=customer_ids)

    return render(request, 'business-customer-list.html', {"users": users})


def about_us(request):
    about_us = AboutUs.objects.filter(business_man=request.user).first()
    
    if request.method == 'POST':
        description = request.POST.get('description', '')
        if about_us:
            about_us.description = description  # Update existing record
            about_us.save()
        else:
            AboutUs.objects.create(description=description, business_man=request.user)  # Create new record
        return redirect('about_us')

    return render(request, 'about-us.html', {"about_us": about_us})
    
def business_man_about_us(request, id):
    about_us = AboutUs.objects.filter(business_man=id).first()
    return render(request, 'about-us.html', {"about_us": about_us})

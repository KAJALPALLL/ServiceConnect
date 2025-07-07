import os

from django.shortcuts import render,redirect
from . models import user_profile
from django.contrib import auth
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required





business_man,created = Group.objects.get_or_create(name='business_man')
customer,created = Group.objects.get_or_create(name='customer')


def register_as_business_man(request):
    try:
        if request.method == "POST":
            first_name = request.POST['first_name']
            phone_number = request.POST['phone_number']
            username = request.POST['username']
            password = request.POST['password']
            profession = request.POST['profession']
            address = request.POST['address']
            description = request.POST['description']
            profile_image = request.FILES['profile_image']

            user_data = user_profile.objects.create_user(username=username,phone_number=phone_number,email=username,password=password,first_name=first_name,
                                                         profession=profession,address=address,description=description,profile_image=profile_image)
            group = Group.objects.get(name='business_man')
            group_data = user_data.groups.add(group)
            group.save()

            return redirect('login')
        else:
            return render(request,'register-businessman.html')
    except Exception as e:
        print(e)
        return redirect('register_as_business_man')


def register_as_customer(request):
    try:
        if request.method == "POST":
            first_name = request.POST['first_name']
            phone_number = request.POST['phone_number']
            username = request.POST['username']
            password = request.POST['password']

            user_data = user_profile.objects.create_user(username=username,phone_number=phone_number,email=username,password=password,first_name=first_name)
            group = Group.objects.get(name='customer')
            group_data = user_data.groups.add(group)
            group.save()
            return redirect('login')
        else:
            return render(request,'register-customer.html')
    except Exception as e:
        print(e)
        return redirect('register_as_customer')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user_data = auth.authenticate(username=username,password=password)
        if user_data is not None:
            auth.login(request,user_data)
            data = user_profile.objects.filter(username=request.user).first()

            request.session['pic'] = f'media/{data.profile_image}'
            return redirect('dashboard')
        else:
            return redirect('login')
    else:
        return render(request,'login.html')



@login_required(login_url='login')
def dashboard(request):
    business_man = user_profile.objects.filter(groups__name="business_man").count()
    customer_data = user_profile.objects.filter(groups__name="customer").count()
    return render(request,'dashboard.html', {"business_man": business_man, "customer_data": customer_data})




def base(request):
    return render(request,'base.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def business_man_list(request):
    business_man_data = user_profile.objects.filter(groups__name='business_man').order_by('-id')
    return render(request,'business-man-list.html',{'data':business_man_data})

@login_required(login_url='login')
def customer_list(request):
    customer_data = user_profile.objects.filter(groups__name='customer').order_by('-id')
    return render(request,'customer-list.html',{'data':customer_data})

@login_required(login_url='login')
def profile(request):
    profile_data = request.user
    user_data = user_profile.objects.filter(username=profile_data).first()
    return render(request,'profile.html',{'data':user_data})

def update_business_man(request,id):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        profession = request.POST['profession']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        description = request.POST['description']
        profile_image = request.POST['profile_image']
        user_profile.objects.filter(id=id).update(first_name=first_name,username=username,profession=profession,phone_number=phone_number,address=address,profile_image=profile_image,description=description)
        return redirect('business_man_list')
    else:
        data = user_profile.objects.filter(id=id).first()
        return render(request,'update-business-man.html',{'data':data})

def delete_business_man(request,id):
    user_data = user_profile.objects.filter(id=id).first()
    if user_data.profile_image:
        os.remove(user_data.profile_image.path)
    user_data.delete()
    return redirect('business_man_list')


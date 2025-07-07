from django.db import models
from user_management.models import user_profile


class Business_History(models.Model):
    business_man = models.ForeignKey(user_profile,on_delete=models.CASCADE,default=None,null=True)
    status = models.CharField(default="Inactive",null=True, max_length=100)
    start_datetime = models.DateTimeField(default=None,null=True)
    end_datetime = models.DateTimeField(default=None,null=True)


class BookAppointment(models.Model):
    business_man = models.ForeignKey(user_profile,on_delete=models.CASCADE,default=None,null=True)
    customer = models.ForeignKey(user_profile,on_delete=models.CASCADE,default=None,null=True,related_name='xyz')
    datetime = models.DateTimeField(default=None,null=True)
    status_choices = (('approved', 'Approved'), ('deny', 'Deny'))
    status = models.CharField(choices=status_choices,default=None,null=True, max_length=50)
    appointment_choices = (('completed', 'Completed'), ('pending', 'Pending'))
    appointment_status = models.CharField(choices=appointment_choices, default=None, null=True, max_length=50)


class Reviews(models.Model):
    description = models.CharField(default=None, null=True, max_length=2000)
    datetime = models.DateTimeField(auto_now_add=True)
    chat_type = (('review', 'Review'), ('conversation', 'Conversation'))
    type = models.CharField(choices=chat_type, max_length=50)
    appointment_booking = models.ForeignKey(BookAppointment, on_delete=models.CASCADE, default=None, null=True)

class Conversation(models.Model):
    description = models.CharField(default=None, null=True, max_length=2000)
    datetime = models.DateTimeField(auto_now_add=True)
    business_man = models.ForeignKey(user_profile,on_delete=models.CASCADE,default=None,null=True)
    customer = models.ForeignKey(user_profile,on_delete=models.CASCADE,default=None,null=True,related_name='ieehfue')
    appointment_booking = models.ForeignKey(BookAppointment, on_delete=models.CASCADE, default=None, null=True)


class AboutUs(models.Model):
    description = models.CharField(default=None, null=True, max_length=2000)
    business_man = models.ForeignKey(user_profile,on_delete=models.CASCADE)

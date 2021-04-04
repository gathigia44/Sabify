from django.shortcuts import render
from .models import User
from django.contrib import messages
from operator import itemgetter
def welcome(req):
	return render(req,'welcome.html')
def login(req):
	return render(req,'login.html')
def register(req):
	if req.method=="POST":
		user = User()

		user.firstname= req.POST['firstname']
		user.lastname= req.POST['lastname']
		user.username= req.POST['username']
		user.email= req.POST['email']
		user.number= req.POST['number']
		user.password= req.POST['password']
		user.repwd= req.POST['repwd']		
		user.street= req.POST['street']
		user.area= req.POST['area']
		user.country= req.POST['country']
		
		user.save()
		messages.success(req,"New User Registered Successfully!")

		



	return render(req,'register.html')		
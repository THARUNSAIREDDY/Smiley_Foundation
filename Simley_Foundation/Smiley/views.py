from django.shortcuts import render,redirect
from django.http import HttpResponse
from Smiley.forms import RegForm,ChpwdForm
from Smiley_Foundation import settings
from .models import Gallary
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib import messages
from Smiley.models import User
from django.contrib.auth.models import User,auth


# Create your views here.

def Home(request):
	return render(request,'html/Home.html',)

def About(request):
	return render(request,'html/About.html')

def Contact(request):
	return render(request,'html/Contact.html')

def Login(request):
	return render(request,'html/Login.html')

def Logout(request):
	return render(request,'html/Logout.html')

def Gallary(request):
	photo=Gallary.objects.all()
	return render(request,'html/Gallary.html',{"photo":photo})

def Register(request):
	# # d=Category.objects.all()
	# if request.method=="POST":
	# 	q=RegForm(request.POST)
	# 	if q.is_valid():
	# 		q.save()
	# 		return redirect('/Login')
	# q=RegForm()
	return render(request,'html/Register.html')

def Profile(request):
	# d=Category.objects.all()
	return render(request,'html/Profile.html')

def cgf(request):
	if request.method=="POST":
		print("yes")
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/Login')
	c=ChpwdForm(user=request)
	return render(request,'html/Changepwd.html',{'t':c})

def UpdateProfile(request):
	if request.method== "POST":
		p=UpdateProfile(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/Profile')
	p= UpdateProfile()
	return render(request,'html/UpdateProfile.html',{'e':p})

def ResetPDone(request):
	return render(request,'html/ResetPDone.html')

def PasswordResetConfirm(request):
	return render(request,'html/PasswordResetConfirm.html')

def PasswordResetComplete(r):
	return render(r,'html/PasswordResetComplete')

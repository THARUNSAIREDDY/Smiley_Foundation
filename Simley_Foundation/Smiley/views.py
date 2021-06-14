from django.shortcuts import render,redirect
from django.http import HttpResponse
from Smiley.forms import SujestionForm,ImForm,UtupForm
from Smiley_Foundation import settings
from .models import Gallary
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib import messages
from Smiley.models import User
from django.contrib.auth.models import User
from Smiley.models import ImProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

def Home(request):
	return render(request,'html/Home.html',)

@login_required(login_url='Login')
def About(request):
	return render(request,'html/About.html')

@login_required(login_url='Login')
def Contact(request):
	return render(request,'html/Contact.html')

def Login(request):
	if request.user.is_authenticated:
		return redirect('Home')
	else:		
		if request.method=="POST":
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('Home')
			else:
				messages.info(request,'username or password is incorrect')
		return render(request,'html/Login.html')

def Logout(request):
	logout(request)
	return render(request,'html/Login.html')

@login_required(login_url='Login')
def Gallary(request):
	photo=Gallary.objects.all()
	return render(request,'html/Gallary.html',{"photo":photo})

def Register(request):
	if request.user.is_authenticated:
		return redirect('Home')
	else:
		q=RegForm()
		if request.method=="POST":
			q=RegForm(request.POST)
			if q.is_valid():
				q.save()
			messages.success(request,"your accout is created Successfully as"+ user)
			return redirect('/Login')
		return render(request,'html/Register.html',{'u':q})

@login_required(login_url='Login')
def dashboard(request):
	return render(request,'html/dashboard.html')

@login_required(login_url='Login')
def Profile(req):
	d=ImForm()
	return render(req,'html/Profile.html',{'d':d})

@login_required(login_url='Login')
def ResetPDone(req):
	return render(req,'html/ResetPDone.html')

@login_required(login_url='Login')
def ResetPassConf(req):
	return render(req,'html/ResetPassConf.html')

@login_required(login_url='Login')
def Reset_Password(req):
	return render(req,'html/Reset_Password.html')

@login_required(login_url='Login')
def Sugestion(req):
	if req.method=="POST":
		data=SujestionForm(req.POST)
		if data.is_valid():
			subject='Confirmation_complaint'
			body="thank you for complaint"+req.POST['p_name']
			receiver=req.POST['p_email']
			sender=settings.EMAIL_HOST_USER
			send_mail(subject,body,sender,[receiver])
			data.save()
			messages.success(req,"Successfully sent to your mail "+receiver)
			return redirect('/')
	form=SujestionForm()
	return render(req,'html/Sugestion.html',{'c':form})



@login_required
def cgf(request):
	if request.method=="POST":
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/Login')

	c=ChpwdForm(user=request)
	return render(request,'stc/Changepwd.html',{'t':c})


@login_required(login_url='Login')
def UpdateProfile(request):
	if request.method == "POST":
		u=UtupForm(request.POST,instance=request.user)
		i=ImForm(request.POST,request.FILES,instance=request.user.improfile)
		if u.is_valid() and i.is_valid():
			u.save()
			i.save()
			return redirect('/Profile')
	u=UtupForm(instance=request.user)
	i=ImForm(instance=request.user.improfile)
	return render(request,'html/UpdateProfile.html',{'us':u,"imp":i})


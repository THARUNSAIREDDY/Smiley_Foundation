from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
# from App.models import User,Worker,Category,Product,Customise,Rolerest
from Smiley.models import User

class RegForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password"
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"
		}))
	class Meta:
		model=User
		fields=['username','email']
		widgets ={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"enter email",
			})
		}

class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter Old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter New password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Confirm your New password"}))
	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']

# class WorkerForm(forms.ModelForm):
# 	class Meta:
# 		model=Worker
# 		fields=["profession","name" ,"phno","gender","Email"]
# 		widgets={
# 		"profession":forms.Select(attrs={
# 			"class":"form-control",
# 			"placeholder":"select category "}),
# 		"name":forms.TextInput(attrs=
# 			{
# 			"class":"form-control",
# 			"placeholder":"Enter your name"
# 			}),
# 		"gender":forms.Select(attrs={"class":"form-control"}),
# 		"Phone no":forms.NumberInput(attrs={"class":"form-control","placeholder":"enter your phone number"}),
# 		"Email":forms.EmailInput(attrs={"class":"form-control","placeholder":"enter email"}),
# 		}
# class CustomiseForm(forms.ModelForm):
# 	class Meta:
# 		model=Customise
# 		fields=["uname","email","phno","category","im","description"]
# 		widgets={
# 		"uname":forms.TextInput(attrs=
# 			{
# 			"class":"form-control",
# 			"placeholder":"Enter your name"
# 			}),
# 		"Phno":forms.NumberInput(attrs={"class":"form-control"}),
# 		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"enter email"}),
# 		"category":forms.Select(attrs={"class":"form-control"}),
		
# 		}
# class CategoryForm(forms.ModelForm):
# 	class Meta:
# 		model=Category
# 		fields='__all__'
	

# class ProductForm(forms.ModelForm):
# 	class Meta:
# 		model=Product
# 		fields='__all__'
class UpPrf(forms.ModelForm):
	class Meta:
		model= User
		fields = ["Name","email","phno","city","state","pin"]
		widgets = {
		"Name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"address"}),
		"email":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"Enter your email"}),
		"phno":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Phone number"}),
		"city":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"city"}),
		"state":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"state"}),
		"pin":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Pincode"}),
		}

# class RoleR(forms.ModelForm):
# 	class Meta:
# 		model = Rolerest
# 		fields= ["roletype"]
# 		widgets={
# 		"uname":forms.TextInput(attrs={"class":"form-control","readonly":True}),

# 		"roletype":forms.Select(attrs = {"class": "form-control",}),
		
# 		}

# class RoleUp(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ["username","role"]
# 		widgets={
# 		"username": forms.TextInput(attrs={"class":"form-control","readOnly":True,}),
# 		"role":forms.Select(attrs={"class":"form-control"}),
# 		}
# class Procustom(forms.ModelForm):
# 	class Meta:
# 		model=Product
# 		fields=["pname","price","description","im"]
# 		widgets={
# 		"pname":forms.TextInput(attrs={"class":"form-control"}),
# 		"price":forms.TextInput(attrs={"class":"form-control"}),
# 		"description":forms.TextInput(attrs={"class":"form-control"})
# 		}
		
		

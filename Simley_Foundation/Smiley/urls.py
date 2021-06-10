from django.urls import path
from Smiley import views #from . import views
from django.contrib.auth import views as ad

urlpatterns = [
    path('',views.Home,name="Home"),
    path('About/',views.About,name="About"),
    path('Contact/',views.Contact,name="Contact"),
    path('Gallary/',views.Gallary,name="Gallary"),
	path('Login/',views.Login,name="Login"),
    path('Logout/',views.Logout,name="Logout"),
    path('Register/',views.Register,name="Register"),
    path('Changepwd/',views.cgf,name="cg"),
	path('Profile/',views.Profile,name='Profile'),
    path('UpdateProfile/',views.UpdateProfile,name="UpdateProfile"),
    path('ResetPDone/',views.ResetPDone,name="ResetPDone"),
    path('rst_cf/<uidb64>/<token>/',views.PasswordResetConfirm,name="password_reset_confirm"),
    path('rst_cmplt/',views.PasswordResetComplete,name="password_reset_complete"),
    
]
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view() ),
    path('verify-otp/', VerifyOtp.as_view() ),
    path('login/', LoginView.as_view() ),
    path('profile/<int:pk>', profile.as_view()),
    path('change-password/', ChangePassword.as_view()),
    path('search/<username>', searchUser.as_view()),
]
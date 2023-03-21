from django.urls import path
from authentication import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name='register'),
    path("verifyotp/", views.VerifyOtpView.as_view(), name='verifyotp')
]

from django.urls import path
from .views import RegisterView, EmailVerifyView, LoginView, LogoutView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email_verify/', EmailVerifyView.as_view(), name='email_verify'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

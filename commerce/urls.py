from django.urls import path, include
from rest_framework import urlpatterns
from django.urls import path
from .views import Payment


urlpatterns = [
    path('payments/', Payment.as_view(), name='payment'),
    #path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]



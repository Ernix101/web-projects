from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tips/', views.GymTipView.as_view(), name='tips'),
    path('register/', views.register, name='register')
]

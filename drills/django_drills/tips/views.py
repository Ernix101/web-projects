from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# Function based view
def home(request):
    return HttpResponse("<h1> Welcome to the Health tip Board<h1>")

# Function based view
def about(request):
    return HttpResponse("<h1>About this app<h1>")

# Class based view
class HealthTipView(View):
    def get(self, request):
        return HttpResponse("<h1>Health tip of the day: Drink more water💧")
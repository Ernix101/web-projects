from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# Function based view
def home(request):
    return HttpResponse("<h1>Looking to get stronger? You're in the right place<h1>")

# Function based view
def about(request):
    return HttpResponse("<h1>About Us, what we are!<h1>")

# Class based view
class GymTipView(View):
    def get(self, request):
        return HttpResponse("<h1>Tip of the day: Keep your core engaged during ab and leg exercises💪🏿<h1>")
    

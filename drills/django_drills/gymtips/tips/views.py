from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import GymTip

# Create your views here.

# Function based view
def home(request):
    tips = GymTip.objects.all()
    return render(request, 'tips/home.html', {'tips': tips})

# Function based view
def about(request):
    return render(request, 'tips/about.html')

# Class based view
class GymTipView(View):
    def get(self, request):
        return render(request, 'tips/tips.html')
    

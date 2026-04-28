from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import GymTip
from .forms import GymTipForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

# Function based view
@login_required
def home(request):
    if request.method == 'POST':
        form = GymTipForm(request.POST)

        if form.is_valid():
            # GymTip.objects.create(
            #     title = form.cleaned_data['title'],
            #     description = form.cleaned_data['description']
            # )
            form.save()
            return redirect('/')
    else:
        form = GymTipForm()

    tips = GymTip.objects.all()
    return render(request, 'tips/home.html', {'tips': tips, 'form': form})

# Function based view
@login_required
def about(request):
    return render(request, 'tips/about.html')

# Class based view
class GymTipView(View):
    def get(self, request):
        return render(request, 'tips/tips.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

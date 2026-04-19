from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import GymTip
from .forms import GymTipForm


# Create your views here.

# Function based view
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
def about(request):
    return render(request, 'tips/about.html')

# Class based view
class GymTipView(View):
    def get(self, request):
        return render(request, 'tips/tips.html')

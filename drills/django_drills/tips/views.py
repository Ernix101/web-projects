from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import HealthTip
from .forms import HealthTipForm

# Create your views here.

# Function based view
def home(request):
    if request.method == 'POST':
        form = HealthTipForm(request.POST)
        
        if form.is_valid():
            # HealthTip.objects.create(
            #     title=form.cleaned_data['title'],
            #     content=form.cleaned_data['content']          <-- We're replacing this part to fit the modelform
            # )
            form.save()                                 # <-- Added form saving to replace the create() block
            return redirect('/')
    else:
        form = HealthTipForm()

    tips = HealthTip.objects.all().order_by('-created_at')  # <-- shows newest first
    return render(request, 'tips/home.html', {'tips': tips, 'form': form})

# Function based view
def about(request):
    return render(request, 'tips/about.html')

# Class based view
class HealthTipView(View):
    def get(self, request):
        return render(request, 'tips/tip.html')
    
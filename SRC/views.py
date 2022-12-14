from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.serializers import serialize
from django.http import JsonResponse
from soybean_metrics.models import *

# Create your views here.
# @login_required(login_url='/accounts/login/')
def base_generic(request):
    p_qs = SoybeanPurchase.objects.all()
    p_data = serialize("json", p_qs) 
    print(p_data*10)
    # return render(request, 'base_generic.html', {})
    return render(request, 'dashboard.html', {"p_data":p_data})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)

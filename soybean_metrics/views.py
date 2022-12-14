from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.serializers import serialize
from django.http import JsonResponse
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def soybean_metrics_home(request): 
    return render(request, 'soybean_metrics_home.html', {})

def get_purchase(request):
    p_qs = SoybeanPurchase.objects.all()
    p_data = serialize("json", p_qs)
    return JsonResponse(p_data, safe=False)

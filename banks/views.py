from django.shortcuts import render
from .models import Bank

# Create your views here.

def show_banks(request):
    object_list = Bank.objects.all()
    return render(request, './banks_page.html', {'object_list':object_list})
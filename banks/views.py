from django.shortcuts import render
from .models import Bank

# Create your views here.

def show_banks(request):
    object_list = Bank.objects.all()
    return render(request, './test_index.html', {'object_list':object_list})
from django.shortcuts import render
from .models import Bank

# Create your views here.

def show_banks(request):
    banks_list = Bank.objects.all()
    for bank in banks_list: bank.phones_format()
    page_title = "OneBank - все банки России"
    return render(request, './banks_page.html', {'object_list': banks_list,
                                                 'page_title':page_title})

def one_bank_info(request,bank_id):
    one_bank = Bank.objects.get(pk=bank_id)
    page_title = "OneBank - все банки"
    return render(request, './one_bank_page.html', {
                                                'one_bank': one_bank,
                                                'page_title': page_title})

from django.db import models

# Create your models here.
class Bank(models.Model):
    bank_name = models.CharField(max_length=100, verbose_name='Наименование банка')
    bank_main_adress = models.CharField(max_length=250, verbose_name='Главный офис')
    bank_phone = models.CharField(max_length=20, verbose_name='Телефон')
    bank_short_desc = models.CharField(max_length=250,verbose_name='описание банка')
    bank_site_url = models.URLField(verbose_name='адрес сайта')
    bank_logo = models.ImageField(verbose_name='Логотип банка')



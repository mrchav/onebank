from django.db import models

# Create your models here.
class Bank(models.Model):
    bank_name = models.CharField(max_length=100, verbose_name='Наименование банка')
    bank_full_name = models.CharField(max_length=100, verbose_name='Полное наименование банка', null=True)
    bank_adress_index = models.CharField(max_length=250, verbose_name='Индекс офиса', null=True)
    bank_main_adress = models.CharField(max_length=250, verbose_name='Главный офис', null=True)
    bank_phone = models.CharField(max_length=20, verbose_name='Телефон')
    bank_short_desc = models.CharField(max_length=250,verbose_name='Описание банка', null=True, blank=True)
    bank_site_url = models.URLField(verbose_name='адрес сайта')
    bank_logo = models.ImageField(verbose_name='Логотип банка', upload_to="bank_logo/")
    bank_license = models.IntegerField(verbose_name='Номер лицензии')
    bank_off_count = models.IntegerField(verbose_name='Кол-во отделений в России', null=True, blank=True)
    bank_fin_deposit = models.BigIntegerField (verbose_name='Вклады/депозиты', null=True, blank=True)
    bank_fin_assets = models.BigIntegerField (verbose_name='активы', null=True, blank=True)
    bank_fin_fiz_credit = models.BigIntegerField(verbose_name='Кредиты физ лицам', null=True, blank=True)
    bank_fin_profit = models.BigIntegerField (verbose_name='Прибыль банка', null=True, blank=True)

    def __str__(self):
        return f'{self.pk} | {self.bank_name}'
    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'

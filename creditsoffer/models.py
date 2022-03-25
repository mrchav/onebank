from django.db import models
#import banks
# Create your models here.

class CreditOffer(models.Model):

    CreditOffer_name = models.CharField(max_length=100, verbose_name='Наименование офера')
    CreditOffer_bank = models.ForeignKey('banks.Bank', on_delete=models.CASCADE)
    CreditOffer_description = models.CharField(max_length=100, verbose_name='Описание оффера', null=True)
    CreditOffer_active = models.BooleanField(default=False, null=True, verbose_name='Активен ли оффер в текущий момент')
    CreditOffer_advert_rate = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Рекламная ставка')
    CreditOffer_sum_min = models.IntegerField(null=False, verbose_name='Минимальная сумма кредита')
    CreditOffer_sum_max = models.IntegerField(null=False, verbose_name='Максимальная сумма кредита')
    CreditOffer_loan_term_min = models.IntegerField(null=False, verbose_name='Минимальная период кредита в месяцах')
    CreditOffer_loan_term_max = models.IntegerField(null=False, verbose_name='Максимальный период кредита в месяцах')
    CreditOffer_review_period = models.CharField(max_length=255, verbose_name='Период рассмотрения', null=True)
    CreditOffer_offer_link_mainfin = models.URLField(verbose_name='адрес ссылки на оффер mainfin', null=False)
    CreditOffer_offer_link = models.URLField(verbose_name='адрес ссылки на оффер', null=False)


    def __str__(self):
        return f'{self.pk} | {self.CreditOffer_name}| {self.CreditOffer_bank}'

    class Meta:
        verbose_name = 'Оффер'
        verbose_name_plural = 'Офферы'

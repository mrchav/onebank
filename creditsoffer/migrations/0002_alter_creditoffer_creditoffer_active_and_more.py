# Generated by Django 4.0.3 on 2022-03-24 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditsoffer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditoffer',
            name='CreditOffer_active',
            field=models.BooleanField(default=False, null=True, verbose_name='Активен ли оффер в текущий момент'),
        ),
        migrations.AlterField(
            model_name='creditoffer',
            name='CreditOffer_advert_rate',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Рекламная ставка'),
        ),
        migrations.AlterField(
            model_name='creditoffer',
            name='CreditOffer_loan_term_max',
            field=models.IntegerField(verbose_name='Максимальный период кредита в месяцах'),
        ),
        migrations.AlterField(
            model_name='creditoffer',
            name='CreditOffer_loan_term_min',
            field=models.IntegerField(verbose_name='Минимальная период кредита в месяцах'),
        ),
        migrations.AlterField(
            model_name='creditoffer',
            name='CreditOffer_sum_max',
            field=models.IntegerField(verbose_name='Максимальная сумма кредита'),
        ),
    ]
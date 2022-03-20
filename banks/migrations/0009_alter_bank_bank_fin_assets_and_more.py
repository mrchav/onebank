# Generated by Django 4.0.3 on 2022-03-20 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0008_alter_bank_bank_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_fin_assets',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='активы'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_fin_deposit',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Вклады/депозиты'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_fin_fiz_credit',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Кредиты физ лицам'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_fin_profit',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Прибыль банка'),
        ),
    ]

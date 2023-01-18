# Generated by Django 3.2.16 on 2023-01-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_dt', models.DateTimeField(auto_now=True)),
                ('order_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('order_surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('order_international', models.CharField(max_length=50, verbose_name='Гражданство')),
                ('order_phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('order_mail', models.CharField(max_length=50, verbose_name='Мэйл')),
                ('order_country', models.CharField(max_length=50, verbose_name='Страна куда хочет')),
                ('order_CV', models.CharField(max_length=50, verbose_name='Его CV')),
                ('order_vakansia', models.CharField(max_length=50, verbose_name='На какую вакансию')),
            ],
        ),
    ]

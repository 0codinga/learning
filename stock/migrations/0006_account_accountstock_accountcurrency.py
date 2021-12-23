# Generated by Django 4.0 on 2021-12-23 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('stock', '0005_stock_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='AccountStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('average_buy_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.account')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock')),
            ],
            options={
                'unique_together': {('account', 'stock')},
            },
        ),
        migrations.CreateModel(
            name='AccountCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.currency')),
            ],
            options={
                'unique_together': {('account', 'currency')},
            },
        ),
    ]
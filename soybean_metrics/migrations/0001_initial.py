# Generated by Django 4.1.3 on 2022-12-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoybeanPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=50)),
                ('purchase_date', models.DateField(blank=True, null=True)),
                ('moisture', models.IntegerField(default=10)),
                ('variety', models.CharField(choices=[('726', 'KDS 726'), ('753', 'KDS 753'), ('1460', 'MACS 1460'), ('335', 'JS 335')], max_length=15)),
                ('quantity', models.IntegerField()),
                ('price_per_unit', models.IntegerField()),
                ('total_payment', models.BigIntegerField(blank=True, null=True)),
                ('payment_done', models.BooleanField()),
                ('discount_percentage', models.IntegerField(default=0)),
                ('payment_details', models.TextField(max_length=250)),
            ],
        ),
    ]
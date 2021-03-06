# Generated by Django 2.2.12 on 2020-09-20 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_prescription_rx_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('generic_name', models.CharField(max_length=100)),
                ('product_ndc', models.CharField(max_length=100)),
                ('dosage_form', models.CharField(max_length=100)),
                ('strength', models.CharField(max_length=100)),
                ('active_ingredient', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]

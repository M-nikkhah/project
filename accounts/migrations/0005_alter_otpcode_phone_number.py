# Generated by Django 4.2.7 on 2023-12-04 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_otpcode_code_alter_otpcode_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن '),
        ),
    ]

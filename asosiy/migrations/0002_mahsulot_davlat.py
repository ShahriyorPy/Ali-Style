# Generated by Django 4.2.4 on 2023-08-10 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='davlat',
            field=models.CharField(default='Uzbekistan', max_length=50, null=True),
        ),
    ]

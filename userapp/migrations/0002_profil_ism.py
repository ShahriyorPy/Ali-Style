# Generated by Django 4.2.4 on 2023-08-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='ism',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
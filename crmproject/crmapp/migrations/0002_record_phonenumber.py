# Generated by Django 4.2.5 on 2023-12-17 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='phonenumber',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
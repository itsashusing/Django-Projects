# Generated by Django 4.2.5 on 2023-12-16 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homeapp', '0003_alter_aboutus_options_alter_aboutus_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={},
        ),
        migrations.AlterModelManagers(
            name='aboutus',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='user',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

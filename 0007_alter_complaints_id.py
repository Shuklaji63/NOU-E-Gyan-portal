# Generated by Django 5.0.6 on 2024-08-31 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egyanportal', '0006_noti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

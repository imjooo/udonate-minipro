# Generated by Django 3.2.14 on 2022-10-15 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_donor_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='role',
            field=models.CharField(default=1, max_length=50, verbose_name='role'),
            preserve_default=False,
        ),
    ]
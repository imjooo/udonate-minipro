# Generated by Django 3.2.14 on 2022-10-22 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20221022_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
    ]

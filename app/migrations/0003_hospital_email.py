# Generated by Django 3.2.14 on 2022-10-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='email',
            field=models.CharField(default=1, max_length=50, verbose_name='email'),
            preserve_default=False,
        ),
    ]

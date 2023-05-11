# Generated by Django 3.2.14 on 2022-09-24 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, verbose_name='username')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
                ('role', models.CharField(max_length=50, verbose_name='role')),
            ],
        ),
        migrations.CreateModel(
            name='donor',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100, verbose_name='fname')),
                ('lname', models.CharField(max_length=100, verbose_name='lname')),
                ('DOB', models.DateField(max_length=100, verbose_name='dob')),
                ('gender', models.CharField(max_length=100, verbose_name='gender')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('ph_no', models.CharField(max_length=100, verbose_name='phn_no')),
                ('blood_grp', models.CharField(max_length=100, verbose_name='blood_grp')),
                ('medical_certificate', models.FileField(upload_to='', verbose_name='medical_certificate')),
                ('last_donate', models.CharField(max_length=100, verbose_name='last_donate')),
                ('district', models.CharField(max_length=100, verbose_name='district')),
                ('logid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.login')),
            ],
        ),
    ]
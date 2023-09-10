# Generated by Django 4.2.4 on 2023-09-07 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='photos/userPhoto')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('author', 'author'), ('reader', 'reader')], max_length=30)),
                ('phone_number', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

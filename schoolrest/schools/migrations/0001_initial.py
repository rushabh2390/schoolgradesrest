# Generated by Django 3.2.16 on 2022-11-26 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('customusermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.customusermodel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('city', models.CharField(default=None, max_length=200)),
                ('pincode', models.CharField(default=None, max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.customusermodel', models.Model),
        ),
    ]

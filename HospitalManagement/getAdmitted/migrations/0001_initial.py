# Generated by Django 5.0.2 on 2024-02-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('admissionDate', models.DateField()),
                ('contact', models.CharField(max_length=11)),
                ('address', models.TextField()),
                ('symptoms', models.TextField()),
            ],
        ),
    ]

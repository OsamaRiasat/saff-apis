# Generated by Django 3.2.5 on 2021-07-31 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0012_dosageforms_packtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='RMDemands',
            fields=[
                ('DNo', models.BigAutoField(primary_key=True, serialize=False)),
                ('Priority', models.CharField(max_length=20)),
                ('DDate', models.DateTimeField(auto_now_add=True)),
                ('CancelledDate', models.DateTimeField()),
                ('PoNo', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
    ]

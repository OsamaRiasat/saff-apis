# Generated by Django 3.2.5 on 2021-08-31 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0002_auto_20210830_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('packSize', models.CharField(max_length=20)),
                ('noOfPacks', models.IntegerField()),
                ('totalPacks', models.IntegerField()),
                ('isRepack', models.BooleanField()),
                ('batchNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bN', to='Production.bprlog')),
            ],
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-01 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PackingMaterialTypes',
            fields=[
                ('Type', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterials',
            fields=[
                ('RMCode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Material', models.CharField(max_length=50)),
                ('Units', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterialTypes',
            fields=[
                ('Type', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='RMDemands',
            fields=[
                ('DNo', models.BigAutoField(primary_key=True, serialize=False)),
                ('DDate', models.DateTimeField(auto_now_add=True)),
                ('CancelledDate', models.DateTimeField(blank=True, null=True)),
                ('PoNo', models.IntegerField(blank=True, max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RMDemandedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Priority', models.CharField(max_length=20)),
                ('DemandedQty', models.FloatField(max_length=10)),
                ('CurrentStock', models.FloatField(default=0, max_length=10)),
                ('QuantityPending', models.FloatField(max_length=10)),
                ('Status', models.CharField(default='Pending', max_length=10)),
                ('DNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.rmdemands')),
                ('RMCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.rawmaterials')),
            ],
        ),
        migrations.AddField(
            model_name='rawmaterials',
            name='Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.rawmaterialtypes'),
        ),
        migrations.CreateModel(
            name='PackingMaterials',
            fields=[
                ('PMCode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Material', models.CharField(max_length=50)),
                ('Units', models.CharField(max_length=10)),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.packingmaterialtypes')),
            ],
        ),
    ]

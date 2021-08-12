# Generated by Django 3.2.5 on 2021-08-12 07:18

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialSuppliers', '0003_alter_supplierapproveditems_id'),
        ('Inventory', '0012_alter_rmreceiving_grno'),
    ]

    operations = [
        migrations.CreateModel(
            name='PMDemands',
            fields=[
                ('DNo', models.BigAutoField(primary_key=True, serialize=False)),
                ('DDate', models.DateTimeField(auto_now_add=True)),
                ('CancelledDate', models.DateTimeField(blank=True, null=True)),
                ('PoNo', models.IntegerField(blank=True, null=True)),
                ('demandStatus', models.CharField(default='PENDING', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PMPurchaseOrders',
            fields=[
                ('PONo', models.BigAutoField(primary_key=True, serialize=False)),
                ('PODate', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(default='PENDING', max_length=10)),
                ('DNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.rmdemands')),
            ],
        ),
        migrations.AlterField(
            model_name='rmbincards',
            name='issued',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='PMReceiving',
            fields=[
                ('IGPNo', models.AutoField(primary_key=True, serialize=False)),
                ('PMCode', models.CharField(max_length=20)),
                ('quantityReceived', models.DecimalField(decimal_places=2, max_digits=10)),
                ('containersReceived', models.IntegerField()),
                ('batchNo', models.CharField(max_length=20, unique=True)),
                ('IGPDate', models.DateTimeField(auto_now_add=True)),
                ('GRNo', models.IntegerField(default=0)),
                ('MFG_Date', models.DateField(blank=True, null=True)),
                ('EXP_Date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='QUARANTINED', max_length=20)),
                ('quantityApproved', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('quantityRejected', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('approval_Date', models.DateField(blank=True, null=True)),
                ('QCNo', models.CharField(blank=True, max_length=20, null=True)),
                ('remarks', models.TextField(blank=True, max_length=100, null=True)),
                ('retest_Date', models.DateField(blank=True, null=True)),
                ('PONo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.pmpurchaseorders')),
                ('S_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MaterialSuppliers.suppliers')),
            ],
        ),
        migrations.CreateModel(
            name='PMPurchaseOrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.FloatField(max_length=10)),
                ('Pending', models.FloatField(blank=True, max_length=10, null=True)),
                ('Received', models.FloatField(default=0, max_length=10)),
                ('Status', models.CharField(default='OPEN', max_length=10)),
                ('CommittedDate', models.DateField(blank=True, null=True)),
                ('Reason', models.CharField(blank=True, max_length=10, null=True)),
                ('PMCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.packingmaterials')),
                ('PONo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.pmpurchaseorders')),
                ('SID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MaterialSuppliers.suppliers')),
            ],
        ),
        migrations.CreateModel(
            name='PMDemandedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Priority', models.CharField(max_length=20)),
                ('DemandedQty', models.FloatField(max_length=10)),
                ('CurrentStock', models.FloatField(default=0, max_length=10)),
                ('QuantityPending', models.FloatField(default=0, max_length=10)),
                ('Status', models.CharField(default='Pending', max_length=10)),
                ('DNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.pmdemands')),
                ('PMCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PCode', to='Inventory.packingmaterials')),
            ],
        ),
        migrations.CreateModel(
            name='PMBinCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateTime', models.DateTimeField(auto_now_add=True)),
                ('particulars', models.CharField(blank=True, max_length=20, null=True)),
                ('batchNo', models.CharField(max_length=20, unique=True)),
                ('received', models.DecimalField(decimal_places=2, max_digits=10)),
                ('issued', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('QCNo', models.CharField(max_length=20)),
                ('GRBalance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PMCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.packingmaterials')),
            ],
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-02 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_alter_rmpurchaseorderitems_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rmdemandeditems',
            name='RMCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RCode', to='Inventory.rawmaterials'),
        ),
    ]

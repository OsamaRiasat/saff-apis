# Generated by Django 3.2.5 on 2021-08-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_alter_rmdemandeditems_rmcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rmdemandeditems',
            name='QuantityPending',
            field=models.FloatField(default=0, max_length=10),
        ),
    ]

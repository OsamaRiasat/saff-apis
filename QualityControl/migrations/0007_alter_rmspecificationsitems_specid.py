# Generated by Django 3.2.5 on 2021-08-23 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QualityControl', '0006_auto_20210823_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rmspecificationsitems',
            name='specID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='QualityControl.rmspecifications'),
        ),
    ]

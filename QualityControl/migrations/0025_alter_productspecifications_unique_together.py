# Generated by Django 3.2.9 on 2022-01-06 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0040_delete_pm_formulation'),
        ('QualityControl', '0024_auto_20210906_0040'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productspecifications',
            unique_together={('ProductCode', 'stage')},
        ),
    ]

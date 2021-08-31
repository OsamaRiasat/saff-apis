# Generated by Django 3.2.5 on 2021-08-30 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bprlog',
            name='currentStage',
            field=models.CharField(default='ISSUED', max_length=20),
        ),
        migrations.AlterField(
            model_name='bprlog',
            name='inProcess',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bprlog',
            name='openingDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bprlog',
            name='yieldPercentage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

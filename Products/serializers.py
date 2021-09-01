from django.db.models import fields
from rest_framework import serializers
from .models import *
from Inventory.models import RawMaterials
from rest_framework.serializers import ValidationError
# Products




# class ProductsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Products
#         fields = '__all__'
#
#
# class PackSizesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PackSizes
#         fields = '__all__'
#
#
# class DosageFormsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DosageForms
#         fields = '__all__'
#
#
#
# class FormulationItemsSerializer(serializers.Serializer):
#     class Meta:
#         model = Formulation
#         fields = ['ProductCode', 'RMCode', 'batchSize', 'quantity', 'date', 'docNo']



class FormulationItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulation

        fields = ['ProductCode', 'RMCode', 'batchSize', 'quantity', 'date', 'docNo', ]


class FormulationSerializer(serializers.ModelSerializer):
    fItems = FormulationItemsSerializer(many=True, write_only=True)

    class Meta:
        model = Formulation
        fields = ['fItems', ]
        # extra_kwargs = {
        #     'DNo': {'read_only': True},
        #     'DDate': {'read_only': True},
        # }
    def validate(self, attrs):
        items = attrs.get('fItems')
        code = items[0]['ProductCode']
        check = Formulation.objects.filter(ProductCode=code)
        if check:
            check.delete()
        return attrs
    def create(self, validated_data):
        items = validated_data.pop('fItems')
        # demand = Formulation.objects.create(**validated_data)
        # demand.save()
        
        obj=""
        for i in items:
            item = Formulation.objects.create(ProductCode=i['ProductCode'],
                                                 RMCode=i['RMCode'],
                                                 batchSize=i['batchSize'],
                                                 quantity=i['quantity'],
                                                 date=i['date'],
                                                 docNo=i['docNo'])
            item.save()
            obj = i
        return obj

#------------New Formulation ------------------#
class PCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['ProductCode',]

class PNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['Product',]

class RMDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterials
        fields = ['RMCode','Material','Units','Type',]

#------------- Edit Formulation -----------------#



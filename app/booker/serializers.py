from rest_framework import serializers
from booker.models import FinanceSheetEntry, FinanceRow, FinanceCategory, FinanceSheet

class FinanceSheetEntryApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceSheetEntry
        fields = '__all__'

    rows = serializers.SerializerMethodField()

    def get_rows(self, instance):
        return FinanceRowApiSerializer(
            FinanceRow.objects.filter(entry=instance),
        many=True).data

    def to_representation(self, instance):
        # Fix me, fails on detailed_route
        #instance.period = instance.period.strftime("%B %Y")
        return super(FinanceSheetEntryApiSerializer, self).to_representation(instance)


class FinanceRowApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceRow
        fields = '__all__'

    category_props = serializers.SerializerMethodField()

    def get_category_props(self, instance):
        return {
            'positive': instance.category.positive,
            'name': instance.category.name,
        }

    def save(self):
        instance = super(FinanceRowApiSerializer, self).save()
        if instance.category.positive:
            instance.amount = abs(instance.amount)
        else:
            instance.amount = -abs(instance.amount)
        instance.save()
        return instance


class FinanceCategoryApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceCategory
        fields = ['id', 'sheet', 'name', 'positive']


class FinanceSheetApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceSheet
        fields = '__all__'
from rest_framework import serializers
from booker.models import FinanceSheetEntry, FinanceRow, FinanceCategory, FinanceSheet
import datetime


class FinanceSheetEntryApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceSheetEntry
        fields = '__all__'

    rows = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()

    def get_rows(self, instance):
        return FinanceRowApiSerializer(
            FinanceRow.objects.filter(entry=instance),
        many=True).data

    def get_categories(self, instance):
        return FinanceCategoryApiSerializer(
            FinanceCategory.objects.filter(sheet=instance.sheet),
        many=True).data

    def to_representation(self, instance):
        # ToDo: resolve multiple call issue
        if isinstance(instance.period, datetime.date):
            instance.period = instance.period.strftime("%B %Y")
        return super(FinanceSheetEntryApiSerializer, self).to_representation(instance)


class FinanceRowApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceRow
        fields = '__all__'
        read_only_fields = ('origin_amount',)


    def to_representation(self, instance):
        # ToDO: dirty code
        category = FinanceCategoryApiSerializer(instance.category).data
        data = super(FinanceRowApiSerializer, self).to_representation(instance)
        data["category"] = category
        return data

class FinanceCategoryApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceCategory
        fields = ['id', 'sheet', 'name', 'positive']


class FinanceSheetApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceSheet
        fields = '__all__'
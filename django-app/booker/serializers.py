from rest_framework import serializers
from booker.models import FinanceSheetEntry, FinanceRow, FinanceCategory, FinanceSheet
import datetime


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
        # ToDo: resolve multiple call issue
        if isinstance(instance.period, datetime.date):
            instance.period = instance.period.strftime("%B %Y")
        return super(FinanceSheetEntryApiSerializer, self).to_representation(instance)


class FinanceRowApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceRow
        fields = '__all__'

    category_name = serializers.SerializerMethodField()
    category_positive = serializers.SerializerMethodField()

    def get_category_name(self, instance):
        return instance.category.name

    def get_category_positive(self, instance):
        return instance.category.positive

class FinanceCategoryApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceCategory
        fields = ['id', 'sheet', 'name', 'positive']


class FinanceSheetApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceSheet
        fields = '__all__'
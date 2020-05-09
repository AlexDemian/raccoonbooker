from rest_framework import serializers
from booker.models import FinanceSheetEntry, EntryRow, FinanceCategory, FinanceSheet
import datetime


class FinanceSheetEntryApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceSheetEntry
        fields = '__all__'

    rows = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()

    def get_rows(self, instance):
        return EntryRowApiSerializer(
            EntryRow.objects.filter(entry=instance),
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


class EntryRowApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntryRow
        fields = ['id', 'name', 'description', 'pinned', 'amount', 'deleted', 'category', 'entry']

class FinanceCategoryApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceCategory
        fields = ['id', 'sheet', 'name', 'positive']


class FinanceSheetApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceSheet
        fields = '__all__'
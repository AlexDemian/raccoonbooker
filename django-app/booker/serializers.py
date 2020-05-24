from rest_framework import serializers
from booker.models import FinanceSheetEntry, EntryRow, FinanceCategory, FinanceSheet
import datetime

class EntryRowApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntryRow
        fields = ['id', 'name', 'description', 'pinned', 'amount', 'deleted', 'category', 'entry']


class FinanceCategoryApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceCategory
        fields = ['id', 'sheet', 'name', 'positive']


class FinanceSheetEntryApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceSheetEntry
        fields = '__all__'

    rows = EntryRowApiSerializer(many=True)
    categories = serializers.SerializerMethodField()

    def to_representation(self, instance):
        # ToDo: resolve multiple call issue
        for field in ['date_from', 'date_to']:
            value = getattr(instance, field)
            if not isinstance(value,  datetime.date):
                continue
            value = value.strftime("%B %d, %Y")
            setattr(instance, field, value)
        return super().to_representation(instance)

    def get_categories(self, instance):
        return FinanceCategoryApiSerializer(
            instance.sheet.categories.all(), many=True
        ).data

class FinanceSheetApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinanceSheet
        fields = '__all__'
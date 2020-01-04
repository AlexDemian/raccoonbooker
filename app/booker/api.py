from rest_framework import viewsets
from booker.models import FinanceSheetEntry, FinanceCategory, FinanceRow, FinanceSheet
from booker.serializers import FinanceSheetEntryApiSerializer, FinanceCategoryApiSerializer, FinanceRowApiSerializer, FinanceSheetApiSerializer
from rest_framework.decorators import action

class FinanceEntryViewSet(viewsets.ModelViewSet):
    model = FinanceSheetEntry
    serializer_class = FinanceSheetEntryApiSerializer

    def get_queryset(self):
        return FinanceSheetEntry.objects.filter(
            sheet__user=self.request.user
        ).order_by('period')


class FinanceCategoryViewSet(viewsets.ModelViewSet):
    model = FinanceCategory
    serializer_class = FinanceCategoryApiSerializer

    def get_queryset(self):
        return FinanceCategory.objects.filter(sheet__user=self.request.user)


class FinanceRowViewSet(viewsets.ModelViewSet):
    model = FinanceRow
    serializer_class = FinanceRowApiSerializer

    def get_queryset(self):
        return FinanceRow.objects.filter(user=self.request.user)


class FinanceSheetViewSet(viewsets.ModelViewSet):
    model = FinanceSheet
    serializer_class = FinanceSheetApiSerializer

    def get_queryset(self):
        return FinanceSheet.objects.filter(user=self.request.user)
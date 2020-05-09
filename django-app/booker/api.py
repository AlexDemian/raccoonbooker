from rest_framework import viewsets
from booker.models import FinanceSheetEntry, FinanceCategory, EntryRow, FinanceSheet
from booker.serializers import FinanceSheetEntryApiSerializer, FinanceCategoryApiSerializer, EntryRowApiSerializer, FinanceSheetApiSerializer
from django_filters.rest_framework import DjangoFilterBackend

class FinanceEntryViewSet(viewsets.ModelViewSet):
    model = FinanceSheetEntry
    serializer_class = FinanceSheetEntryApiSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['period', 'sheet']

    def get_queryset(self):
        return FinanceSheetEntry.objects.filter(
            sheet__user=self.request.user
        ).order_by('period')


class FinanceCategoryViewSet(viewsets.ModelViewSet):
    model = FinanceCategory
    serializer_class = FinanceCategoryApiSerializer

    def get_queryset(self):
        return FinanceCategory.objects.filter(sheet__user=self.request.user)


class EntryRowViewSet(viewsets.ModelViewSet):
    model = EntryRow
    serializer_class = EntryRowApiSerializer

    def get_queryset(self):
        return EntryRow.objects.filter(entry__sheet__user=self.request.user)


class FinanceSheetViewSet(viewsets.ModelViewSet):
    model = FinanceSheet
    serializer_class = FinanceSheetApiSerializer

    def get_queryset(self):
        return FinanceSheet.objects.filter(user=self.request.user)
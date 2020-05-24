from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from booker.models import FinanceSheetEntry, FinanceCategory, EntryRow, FinanceSheet
from booker.serializers import FinanceSheetEntryApiSerializer, FinanceCategoryApiSerializer, EntryRowApiSerializer, FinanceSheetApiSerializer
from booker.permissions import isEntryOwner, isSheetOwner, isOwner, isCategoryOwner

class ObjectPermissionedModelViewSet(viewsets.ModelViewSet):
    
    def perform_create(self, serializer):
        obj = self.model(**serializer.validated_data)
        self.check_object_permissions(self.request, obj)
        super().perform_create(serializer)


class FinanceEntryViewSet(ObjectPermissionedModelViewSet):
    model = FinanceSheetEntry
    serializer_class = FinanceSheetEntryApiSerializer
    filterset_fields = {
        'name': ['icontains'],
        'date_from': ['gte', 'lte', 'exact'],
        'date_to': ['gte', 'lte', 'exact'],
        'sheet': ['exact']
    }
    permission_classes = [isSheetOwner, IsAuthenticated]

    def get_queryset(self):
        return FinanceSheetEntry.objects.filter(
            sheet__user=self.request.user
        ).order_by('date_from')


class FinanceCategoryViewSet(ObjectPermissionedModelViewSet):
    model = FinanceCategory
    serializer_class = FinanceCategoryApiSerializer
    permission_classes = [isSheetOwner, IsAuthenticated]

    def get_queryset(self):
        return FinanceCategory.objects.filter(sheet__user=self.request.user)


class EntryRowViewSet(ObjectPermissionedModelViewSet):
    model = EntryRow
    serializer_class = EntryRowApiSerializer
    permission_classes = [isCategoryOwner, isEntryOwner,  IsAuthenticated]
    
    def get_queryset(self):
        return EntryRow.objects.filter(
            entry__sheet__user=self.request.user,
            category__sheet__user=self.request.user
        )

class FinanceSheetViewSet(ObjectPermissionedModelViewSet):
    model = FinanceSheet
    serializer_class = FinanceSheetApiSerializer
    permission_classes = [isOwner, IsAuthenticated]

    def get_queryset(self):
        return FinanceSheet.objects.filter(user=self.request.user)
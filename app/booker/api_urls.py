from booker.api import FinanceEntryViewSet, FinanceCategoryViewSet, FinanceRowViewSet, FinanceSheetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'entries', FinanceEntryViewSet, basename='api-entries')
router.register(r'categories', FinanceCategoryViewSet, basename='api-categories')
router.register(r'rows', FinanceRowViewSet, basename='api-rows')
router.register(r'sheets', FinanceSheetViewSet, basename='api-sheets')
urlpatterns = router.urls
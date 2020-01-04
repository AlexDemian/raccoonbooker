from booker.api import FinanceEntryViewSet, FinanceCategoryViewSet, FinanceRowViewSet, FinanceSheetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'entries', FinanceEntryViewSet, basename='entries')
router.register(r'categories', FinanceCategoryViewSet, basename='categories')
router.register(r'rows', FinanceRowViewSet, basename='rows')
router.register(r'sheets', FinanceSheetViewSet, basename='sheets')
urlpatterns = router.urls
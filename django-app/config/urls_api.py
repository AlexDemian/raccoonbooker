from profiles.api import UserModelViewSet
from booker.api import FinanceEntryViewSet, FinanceCategoryViewSet, EntryRowViewSet, FinanceSheetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'booker/entries', FinanceEntryViewSet, basename='api-entries')
router.register(r'booker/categories', FinanceCategoryViewSet, basename='api-categories')
router.register(r'booker/rows', EntryRowViewSet, basename='api-rows')
router.register(r'booker/sheets', FinanceSheetViewSet, basename='api-sheets')
router.register(r'profiles/users', UserModelViewSet, basename='api-users')
urlpatterns = router.urls
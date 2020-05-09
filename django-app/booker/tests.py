from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from booker.models import EntryRow, FinanceCategory, FinanceSheet, FinanceSheetEntry, Wish
from booker.factories import UserFactory, EntryRowFactory
User = get_user_model()

# ToDo: finish tests

class DemoSessionTestCase(TestCase):

    def setUp(self):
        self.url = reverse('base-content-generator')

    def test_demo_session(self):
        response = self.client.post(self.url)
        self.assertEqual(len(User.objects.all()), 1)
        self.assertEqual(len(FinanceSheet.objects.all()), 1)
        self.assertEqual(len(FinanceSheetEntry.objects.all()), 1)
        self.assertEqual(len(FinanceCategory.objects.all()), 2)
        self.assertEqual(len(Wish.objects.all()), 1)


class BookerAPITestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.client._login(self.user)

    def test_ok_on_get(self):
        urls = [
            reverse('api-entries-list'),
            reverse('api-sheets-list'),
            reverse('api-categories-list'),
            reverse('api-rows-list')
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_sheets_api(self):
        pass

    def test_entries_api(self):
        pass

    def test_categories_api(self):
        pass

    def test_rows_api(self):
        pass
        """Fix me
        row = EntryRowFactory.create(
            entry__sheet__user=self.user,
            category__sheet__user=self.user
        )
        url = '/api/booker/rows/%s/' % row.id
        row.amount = 100
        response = self.client.put(url, data={'id': row.id, 'amount': row.amount}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(EntryRow.objects.get(pk=row.pk).amount, -100)
        """
import factory
from booker.models import FinanceSheet, FinanceCategory, FinanceSheetEntry, FinanceRow, Wish
from django.contrib.auth import get_user_model
import random
import time
import datetime

class UserFactory(factory.django.DjangoModelFactory):
    password = '123'

    class Meta:
        model = get_user_model()


class FinanceSheetFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    name = 'Home'

    class Meta:
        model = FinanceSheet


class FinanceCategoryFactory(factory.django.DjangoModelFactory):
    sheet = factory.SubFactory(FinanceSheetFactory)
    name = random.choice(['Meal', 'Utilities'])
    positive = False

    class Meta:
        model = FinanceCategory


class FinanceSheetEntryFactory(factory.django.DjangoModelFactory):
    sheet = factory.SubFactory(FinanceSheetFactory)
    name = 'New sheet entry'
    period = datetime.datetime.now()

    class Meta:
        model = FinanceSheetEntry


class FinanceRowFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(FinanceCategoryFactory)
    entry = factory.SubFactory(FinanceSheetEntryFactory)
    name = 'Wine'
    amount = 3.5

    class Meta:
        model = FinanceRow


class WishFactory(factory.django.DjangoModelFactory):
    name = 'New car'
    description = 'Cool red funny car!'
    sheet = factory.SubFactory(FinanceSheetFactory)
    amount = 18500
    expected_date = datetime.datetime.now() + datetime.timedelta(days=180)

    class Meta:
        model = Wish


class BaseContentFactory:

    @staticmethod
    def create(user):
        sheet = FinanceSheetFactory.create(user=user)
        categories = [
            FinanceCategoryFactory.create(
                sheet=sheet,
                name='New laptop'
            ),
            FinanceCategoryFactory.create(
                sheet=sheet,
                name='Money incomings',
                positive=True
            ),
        ]
        entry = FinanceSheetEntryFactory.create(sheet=sheet)
        activities = [
            FinanceRowFactory.create(
                name='new fucking necklace',
                category=categories[0],
                entry=entry,
                amount=-100500,
            ),
            FinanceRowFactory.create(
                name='Sallary',
                category=categories[1],
                entry=entry,
                amount=100500,
            )
        ]
        wish = WishFactory.create(sheet=sheet)
        return locals()


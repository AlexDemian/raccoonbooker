import random
import names
import datetime
import time

from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
import factory

from booker.models import FinanceSheet, FinanceCategory, FinanceSheetEntry, EntryRow, Wish

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = get_user_model()

    @factory.lazy_attribute
    def password(self):
        return get_random_string(length=20)

    @factory.lazy_attribute
    def email(self):
        return '{}_{}@foo.com'.format(names.get_first_name(), int(time.time()))

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


class EntryRowFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(FinanceCategoryFactory)
    entry = factory.SubFactory(FinanceSheetEntryFactory)
    name = 'Wine'
    amount = 3.5

    class Meta:
        model = EntryRow


class WishFactory(factory.django.DjangoModelFactory):
    name = 'New car'
    description = 'Cool red funny car!'
    sheet = factory.SubFactory(FinanceSheetFactory)
    amount = 18500
    expected_percent = 2

    @factory.lazy_attribute
    def expected_date(self):
        return datetime.datetime.now() + datetime.timedelta(days=180)

    class Meta:
        model = Wish


class BaseContentFactory:

    @staticmethod
    def create(user):
        sheet = FinanceSheetFactory.create(user=user)
        categories = [
            FinanceCategoryFactory.create(
                sheet=sheet,
                name='Technical needs'
            ),
            FinanceCategoryFactory.create(
                sheet=sheet,
                name='Money incomings',
                positive=True
            ),
        ]
        entry = FinanceSheetEntryFactory.create(sheet=sheet)
        activities = [
            EntryRowFactory.create(
                name='New laptop',
                category=categories[0],
                entry=entry,
                amount=-1000,
            ),
            EntryRowFactory.create(
                name='Sallary',
                category=categories[1],
                entry=entry,
                amount=100500,
            )
        ]
        wish = WishFactory.create(sheet=sheet)
        return locals()


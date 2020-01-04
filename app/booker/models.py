from django.db import models
from django.contrib.auth import get_user_model

class FinanceSheet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'booker_sheets'


class FinanceCategory(models.Model):
    sheet = models.ForeignKey(FinanceSheet, on_delete=models.CASCADE)
    name = models.CharField(default=sheet.name, max_length=100)
    positive = models.BooleanField()

    class Meta:
        db_table = 'booker_categories'


class FinanceSheetEntry(models.Model):
    sheet = models.ForeignKey(FinanceSheet, on_delete=models.CASCADE)
    period = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'booker_entry'


class FinanceRow(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(FinanceCategory, on_delete=models.CASCADE)
    entry = models.ForeignKey(FinanceSheetEntry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True, max_length=200)
    pinned = models.BooleanField(default=False)
    amount = models.FloatField()

    class Meta:
        db_table = 'booker_rows'

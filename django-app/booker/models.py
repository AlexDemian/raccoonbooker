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
    category = models.ForeignKey(FinanceCategory, on_delete=models.CASCADE)
    entry = models.ForeignKey(FinanceSheetEntry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=200)
    pinned = models.BooleanField(default=False)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    origin_amount = models.DecimalField(decimal_places=2, max_digits=20)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'booker_rows'

    def save(self, *args, **kwargs):
        first_save = self.pk is None
        if first_save:
            self.origin_amount = self.amount

        if self.category.positive:
            self.amount = abs(self.amount)
        else:
            self.amount = -abs(self.amount)

        return super(FinanceRow, self).save(*args, **kwargs)


class Wish(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    sheet = models.ForeignKey(FinanceSheet, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=200)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=20)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    deleted = models.BooleanField(default=False)
    expected_date =  models.DateField()

    class Meta:
        db_table = 'booker_wishlist'
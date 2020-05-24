from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

class FinanceSheet(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="sheets")
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'booker_sheets'
        unique_together = ('user', 'name')


class FinanceCategory(models.Model):
    sheet = models.ForeignKey(FinanceSheet, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(default=sheet.name, max_length=100)
    positive = models.BooleanField()

    class Meta:
        db_table = 'booker_categories'


class FinanceSheetEntry(models.Model):
    sheet = models.ForeignKey(FinanceSheet, on_delete=models.CASCADE, related_name="entries")
    date_from = models.DateField()
    date_to = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'booker_entry'


class GenericFinanceRow(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(FinanceCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=20)

    class Meta:
        abstract = True

class TemplatedRow(GenericFinanceRow):
    sheet = models.ForeignKey(FinanceSheet, on_delete=models.CASCADE)

    class Meta:
        db_table = 'booker_templated_rows'

class EntryRow(GenericFinanceRow):
    entry = models.ForeignKey(FinanceSheetEntry, on_delete=models.CASCADE, related_name="rows")
    description = models.CharField(blank=True, max_length=200)
    pinned = models.BooleanField(default=False)
    origin_amount = models.DecimalField(decimal_places=2, max_digits=20)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'booker_rows'
        unique_together = ('name', 'entry', 'category')

    def save(self, *args, **kwargs):
        first_save = self.pk is None
        if first_save:
            self.origin_amount = self.amount

        if self.category.positive:
            self.amount = abs(self.amount)
        else:
            self.amount = -abs(self.amount)

        return super(EntryRow, self).save(*args, **kwargs)


class Wish(models.Model):
    sheet = models.ForeignKey(FinanceSheet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=200)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=20)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    deleted = models.BooleanField(default=False)
    expected_date =  models.DateField()
    expected_percent = models.DecimalField(validators=[MinValueValidator(.1), MaxValueValidator(100)], decimal_places=2, max_digits=3)
    
    class Meta:
        db_table = 'booker_wishlist'
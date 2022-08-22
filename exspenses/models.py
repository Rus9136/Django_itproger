from django.db import models

# Create your models here.
class expenses(models.Model):
    expenses_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Наименование расхода')
    category = models.CharField(max_length=200, verbose_name='Категория')
    expense = models.IntegerField(verbose_name='Расход')
    comment = models.CharField(max_length=300, verbose_name='Коментарии', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'
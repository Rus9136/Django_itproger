from django.db import models


class afisha_model(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование мероприятия')
    date = models.CharField(max_length=200, verbose_name='Дата и время')




    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'



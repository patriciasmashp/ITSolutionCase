from django.db import models

from Directory.models import Status, Type, Category, Subcategory


class Payment(models.Model):

    class Meta:
        verbose_name_plural = 'ДДС'

    create_date = models.DateTimeField(verbose_name='Дата создания',
                                       auto_now_add=True)
    status = models.ForeignKey(Status,
                               on_delete=models.CASCADE,
                               verbose_name='Статус ДДС')
    payment_type = models.ForeignKey(Type,
                                     on_delete=models.CASCADE,
                                     verbose_name='Тип ДДС')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория ДДС')
    subcategory = models.ForeignKey(Subcategory,
                                    on_delete=models.CASCADE,
                                    verbose_name='подкатегория ДДС')
    amount = models.FloatField(verbose_name='Сумма')
    comment = models.TextField(verbose_name='Комментарий',
                               default='',
                               blank=True)

    def __str__(self):
        return self.create_date.strftime('%D-%M-%Y %H:%M') + ' ' + str(
            self.subcategory)

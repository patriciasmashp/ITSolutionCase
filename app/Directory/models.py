from django.db import models
from django.urls import reverse

# Create your models here.


# Create your models here.
class Status(models.Model):

    class Meta:
        verbose_name_plural = 'Статусы'

    name = models.CharField(verbose_name='Название статуса', max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):

    class Meta:
        verbose_name_plural = 'Типы'

    name = models.CharField(verbose_name='Название типа', max_length=100)
    
    def get_absolute_url(self): # new
        return reverse('index')

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Категории'

    name = models.CharField(verbose_name='Название категории', max_length=100)
    category_type = models.ForeignKey(Type,
                                      on_delete=models.CASCADE,
                                      verbose_name='Тип',
                                      related_name='categories')

    def __str__(self):
        return self.name


class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Подкатегории'

    name = models.CharField(verbose_name='Название подкатегории',
                            max_length=100)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='subcategories',
                                 verbose_name='Категория')

    def __str__(self):
        return self.name

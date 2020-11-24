from django.db import models
from random import randint, choice
from django.utils.crypto import get_random_string
from django.db import models


class Search(models.Model):
    id = models.IntegerField(default=True, primary_key=True, verbose_name='id', auto_created=True).hidden
    link = models.CharField(max_length=100, blank=False,  verbose_name='Запрос')
    region = models.CharField(max_length=100, blank=False, verbose_name='Регион')


    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return self.link
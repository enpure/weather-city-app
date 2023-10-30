from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='Город')

    def __str__(self):
        return f'{self.name}'

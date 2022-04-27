from django.db import models
from django_postgres_extensions.models.fields import ArrayField


# Create your models here.
class Images(models.Model):
    image = models.ImageField('Путь до изображения', db_index=True, upload_to='uploadedimages/')

    def __str__(self):
        return str(self.pk)


class BoxWithoutMask(models.Model):
    x = models.IntegerField('Х левый верхний')
    y = models.IntegerField('Y левый верхний')
    width = models.IntegerField('Ширина')
    height = models.IntegerField('Высота')
    source_image = models.ForeignKey('Images', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.pk)

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=200)
    content = RichTextField(verbose_name='Contenido')
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'

    def __str__(self):
        return self.title
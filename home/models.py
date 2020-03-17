from django.db import models
from ckeditor.fields import RichTextField


class post(models.Model):
    title = models.CharField(max_length=120,verbose_name='Baslik')
    home_text = models.TextField(max_length=5000,verbose_name='Anasayfa Yazisi')
    text = RichTextField(verbose_name='Yazi')
    code = models.TextField(verbose_name='Kod',blank=True)
    publish_date = models.DateField(verbose_name='tarih')

    def __str__(self):
        return self.title


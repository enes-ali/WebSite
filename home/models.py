from django.db import models
from ckeditor.fields import RichTextField


class post(models.Model):
    title = models.CharField(max_length=120,verbose_name='Baslik')
    home_text = models.TextField(max_length=5000,verbose_name='Anasayfa Yazisi')
    text = RichTextField(verbose_name='Yazi')

    choices = (
        ('#OpenCV', 'OpenCV'),
        ('c++', 'c++'),
        ('python', 'python'),
        ('css', 'css'),
        ('html', 'html'),
    )
    choice = models.CharField(max_length=30,choices=choices,verbose_name='Konu')

    publish_date = models.DateField(verbose_name='tarih')

    def __str__(self):
        return self.title


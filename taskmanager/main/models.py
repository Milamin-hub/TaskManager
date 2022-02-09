from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    content = models.TextField('Описание', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задания'
        verbose_name_plural = 'Задание'
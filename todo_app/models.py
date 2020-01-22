from django.db import models
from django.urls import reverse
# from . import views
# Create your models here.


class item(models.Model):
    title = models.CharField(blank=True, max_length=50)
    text = models.TextField()

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        if self.title == '':
            return "No title"
        else:
            return self.title

    def get_absolute_url(self):
        return reverse("todo_app:detail", kwargs={'pk': self.pk})

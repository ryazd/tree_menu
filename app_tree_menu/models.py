from django.db import models
from django.urls import reverse

class MenuObj(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True,
                            blank=True, 
                            related_name='children',
                            on_delete=models.CASCADE)
    url = models.CharField(max_length=100)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app_menu:draw_menu', args=[self.url])

from django.db import models
from django.urls import reverse


class Phone(models.Model):
    image = models.ImageField(upload_to='phones/', default='phones/default.png')
    model_name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.FloatField()
    color = models.CharField(max_length=200)
    operation_system = models.CharField(max_length=200)
    screen_size = models.FloatField()
    preview_text = models.TextField()
    rating = models.IntegerField()
    camera_resolution = models.FloatField()
    stock_quantity = models.IntegerField()
    storage = models.IntegerField(default=128)
    
    def __str__(self):
        return f'{self.brand} {self.model_name}'
    
    def get_absolute_url(self):
        return reverse('phone-detail', args=[str(self.id)])

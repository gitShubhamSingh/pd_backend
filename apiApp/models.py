import os
from django.db import models
from django.conf import settings

class Property(models.Model):
    propertyName = models.CharField(max_length=255)
    availableFor = models.CharField(max_length=50)
    totalPrice = models.CharField(max_length=255)
    perSqFeetPrice = models.CharField(max_length=255)
    propertyType = models.CharField(max_length=50)
    bedroom = models.CharField(max_length=255)
    bathroom = models.CharField(max_length=255)
    parking = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    address = models.TextField()
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.id} - {self.property_name}"

    def get_image_folder_path(self):
        return os.path.join(settings.MEDIA_ROOT, f"property_images/{self.id}")

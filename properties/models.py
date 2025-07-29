from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class Developer(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Subdivision(models.Model):
    name = models.CharField(max_length=255)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Property(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('sold', 'Sold'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True, blank=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.TextField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    google_maps_link = models.URLField(blank=True, null=True)
    lot_area_sqm = models.DecimalField(max_digits=10, decimal_places=2)
    floor_area_sqm = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/', storage=MediaCloudinaryStorage())

    def __str__(self):
        return f"{self.property.title} Image"

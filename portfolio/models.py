from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Portfolio(models.Model):
    coverimage = models.ImageField(upload_to = 'uploads/',blank=True, null=True)
    projectdetailimage = models.ImageField(upload_to = 'uploads/',blank=True, null=True)
    title  = models.CharField(max_length=250)
    date = models.DateField()
    services = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    details = RichTextField()

    def __str__(self):
        return self.title
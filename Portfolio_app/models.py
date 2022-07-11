from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField()
    def __str__(self):
        return '%s' % (self.name)
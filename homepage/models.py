from django.db import models


# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='activities/images/')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Description(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='description/images/', blank=True)
    TYPE_CHOICES = (
        ('personal', 'Personal'),
        ('education', 'Education'),
        ('jobs', 'Jobs'),
        ('career', 'Career goals'),
        ('skills', 'Skills'),

    )
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='personal')
    company = models.CharField(max_length=100, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone

class Breed(models.Model):
    breedType = models.CharField(max_length=100)

    def __str__(self):
        return self.breedType

class Dog(models.Model):
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    breed = models.ForeignKey(Breed, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(max_length=8, choices=gender_choices, default='male')
    image = models.ImageField(default='default.jpg', upload_to='dog_pictures')
    time_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['age']

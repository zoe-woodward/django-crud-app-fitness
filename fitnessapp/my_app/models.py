from django.db import models
from django.urls import reverse

class Workout(models.Model):
    name = models.CharField(max_length=100)
    image_filename = models.CharField(max_length=255, default='images/logo.avif')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('workout-detail', kwargs={'workout_id': self.id})




class Activity(models.Model):
    date = models.DateField()
    length= models.CharField(max_length=10)
    description=models.CharField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)


    def __str__(self):
        return f"You completed {self.length} of {self.workout.name} on {self.date}"
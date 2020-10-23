from django.db import models

#this model contains do's and dont's for different  diseases and what regular checkups and exercises elders must have to do.
class Healthdata(models.Model):
    disease = models.TextField(max_length=50)
    Dos=models.TextField()
    Donts=models.TextField()
    checkups=models.TextField()
    Exercise=models.TextField()
    def __str__(self):
        return self.disease


    
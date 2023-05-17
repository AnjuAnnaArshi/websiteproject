from django.db import models

# Create your models here.
class places(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name
class team(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    about=models.TextField()

    def __str__(self):
        return self.name
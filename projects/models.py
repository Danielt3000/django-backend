from django.db import models
from cloudinary.models import CloudinaryField



class Project(models.Model):
    
    name = models.CharField(max_length=18)

    about = models.CharField(max_length=200)

    github= models.CharField(max_length=400)

    url = models.CharField(max_length=300)


    


    image = CloudinaryField(
        'image', blank=True, null=False,
    )

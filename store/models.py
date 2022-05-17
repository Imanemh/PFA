from django.db import models

class Post(models.Model) :
    images = models.FileField(upload_to='static/images/') 

# Create your models here.

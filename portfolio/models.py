from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100) # no more than 100 characters in these titles
    description = models.CharField(max_length=250) # no more than 250 characters in these descriptions
    image = models.ImageField(upload_to='portfolio/images/') #where the images are going to be uploaded to for this app
    url = models.URLField(blank=True) #blank=True makes any attribute optional

    def __str__(self):
        return self.title

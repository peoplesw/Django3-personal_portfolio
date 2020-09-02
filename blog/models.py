from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) # takes a string with max 200 characters
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.title

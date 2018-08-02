from django.db import models

# Create your models here.
class Screenshot(models.Model):
    url = models.TextField()

    def __str__(self):
        return "#{}: Screenshot of {}".format(self.id,self.url)

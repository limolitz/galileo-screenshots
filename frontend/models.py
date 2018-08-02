from django.db import models

# Create your models here.
class Screenshot(models.Model):
    url = models.TextField()
    screenshot_name = models.CharField(max_length=64,default=None, blank=True, null=True)

    def __str__(self):
        return "#{}: Screenshot of {}".format(self.id,self.url)

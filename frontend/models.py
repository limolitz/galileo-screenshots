from django.db import models

# Create your models here.
class Screenshot(models.Model):
    url = models.URLField()
    screenshot_name = models.CharField(max_length=64, default="", blank=True)
    request_time = models.DateTimeField(auto_now_add=True)
    screenshot_time = models.DateTimeField(blank=True, null=True)
    user_agent = models.CharField(max_length=128, default="", blank=True)


    def __str__(self):
        return "#{}: Screenshot of {}".format(self.id,self.url)

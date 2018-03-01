from django.db import models

# Create your models here.
class Sabscriber(models.Model):
    sabscriber_name = models.CharField(max_length=200)
    sabscriber_email = models.EmailField()
    def __str__(self):
        return "User: %s" %(self.sabscriber_name)
    class Meta():
        verbose_name = "Sabscriber"
        verbose_name_plural = "All Subscribers"


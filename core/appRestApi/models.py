from django.db import models

# Create your models here.
class apiModel(models.Model):
    app_name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.app_name
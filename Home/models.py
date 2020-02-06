from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self):
        return self.title

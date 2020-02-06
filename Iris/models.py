from django.db import models


class IrisData(models.Model):
    date_posted = models.DateTimeField(auto_now=True)
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    prediction = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.prediction

from django.db import models


class IrisData(models.Model):
    date_posted = models.DateTimeField(auto_now=True)
    sepal_length = models.FloatField(verbose_name='Sepal Length (cm)')
    sepal_width = models.FloatField(verbose_name='Sepal Width (cm)')
    petal_length = models.FloatField(verbose_name='Petal Length (cm)')
    petal_width = models.FloatField(verbose_name='Petal Width (cm)')
    prediction = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.prediction

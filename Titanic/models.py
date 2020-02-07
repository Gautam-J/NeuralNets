from django.db import models


class TitanicData(models.Model):

    GENDER_CHOICES = (('male', 'Male'),
                      ('female', 'Female'))

    P_CLASS_CHOICES = ((1, 'First Class'),
                       (2, 'Second Class'),
                       (3, 'Third Class'))

    date_posted = models.DateTimeField(auto_now=True)
    passenger_class = models.IntegerField(choices=P_CLASS_CHOICES)
    sex = models.CharField(max_length=50, choices=GENDER_CHOICES)
    age = models.IntegerField()
    siblings_or_spouse = models.IntegerField()
    parents_or_children = models.IntegerField()
    fare = models.FloatField()
    prediction = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.prediction

from django.db import models
import datetime as dt


class Visit(models.Model):
    HOUR_CHOICES = [
        (1, 'За час'),
        (2, 'За 2 часа'),
        (4, 'За 4 часа'),
        (24, 'За день'),
        (168, 'За неделю')
    ]

    name_visit = models.CharField(max_length=100)
    date_of_visit = models.DateField()
    time_to_remind = models.PositiveIntegerField(choices=HOUR_CHOICES)

    def __str__(self):
        return self.name_visit
# Create your models here.

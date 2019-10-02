from django.db import models
import datetime as dt
from celery.decorators import periodic_task
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import send_mail


class Visit(models.Model):
    HOUR_CHOICES = [
        (1, 'За час'),
        (2, 'За 2 часа'),
        (4, 'За 4 часа'),
        (24, 'За день'),
        (168, 'За неделю')
    ]

    name_visit = models.CharField(max_length=100)
    date_of_visit = models.DateTimeField()
    time_to_remind = models.PositiveIntegerField(choices=HOUR_CHOICES)
    date_of_ring_for_visit = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, **kwars):
        self.date_of_ring_for_visit = self.date_of_visit
        for i in range(self.time_to_remind):
            self.date_of_ring_for_visit -= dt.timedelta(hours=1)
        super().save(**kwars)

    def __str__(self):
        return self.name_visit

    def go_send(self):
        if timezone.now() > self.date_of_ring_for_visit:
            send_mail(self.name_visit,
                      'you are going to ' + self.name_visit + str(self.date_of_visit),
                      'bkozlovsky@bk.ru',
                      self.user.email)


@periodic_task(run_every=dt.timedelta(seconds=10))
def check_visit():
    print('hello')
    #for visit in Visit.objects.all():
    #    visit.go_send()


from django.db import models
from django.utils.translation import ugettext_lazy as _

WEEKDAYS = [
  (0, _("Monday")),
  (1, _("Tuesday")),
  (2, _("Wednesday")),
  (3, _("Thursday")),
  (4, _("Friday")),
  (5, _("Saturday")),
  (6, _("Sunday")),
]

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    minimum_order = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)

    def opened_on(self, dt):
        """Return True if Restaurant is open on given datetime"""
        qs = self.opening_hours.filter(week_day=dt.weekday())
        qs = qs.filter(start__lte=dt.time(), end__gt=dt.time())
        return qs.exists()

class OpeningHour(models.Model):
    week_day = models.IntegerField(choices=WEEKDAYS)
    start = models.TimeField()
    end = models.TimeField()
    place = models.ForeignKey(Restaurant, related_name='opening_hours')

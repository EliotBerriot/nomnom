import datetime

from nomnom.tests.base import NomNomTestCase
from nomnom.places import models


class PlacesModelsTestCase(NomNomTestCase):

    def setUp(self):
        super().setUp()
        self.place = models.Restaurant(name='Question de gouts')
        self.place.save()

    def test_opening_hours(self):
        now = datetime.datetime(2015, 10, 12, 10, 30)
        opening_hour = models.OpeningHour(start=datetime.time(8, 30),
                                          end=datetime.time(12, 30),
                                          place=self.place,
                                          week_day=now.weekday())
        opening_hour.save()
        self.assertTrue(self.place.opened_on(now))
        self.assertFalse(self.place.opened_on(now + datetime.timedelta(hours=5)))

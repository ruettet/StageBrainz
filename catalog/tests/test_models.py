from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from datetime import datetime

from catalog.models import EntityShow, EntityProduction, EntitySeason, EntityOrganity


class EntityShowModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        EntityShow.objects.create(name='show', when_date=datetime(1970,1,1,1,0,0).date(), when_time=datetime(1970,1,1,1,0,0).time())
        EntityShow.objects.create(name='show', when_date=datetime(1970, 1, 1, 1, 0, 0).date())

    def test_name_label(self):
        show = EntityShow.objects.get(id=1)
        field_label = show._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_when_date_label(self):
        show = EntityShow.objects.get(id=1)
        field_label = show._meta.get_field('when_date').verbose_name
        self.assertEquals(field_label, 'when date')

    def test_when_time_label(self):
        show = EntityShow.objects.get(id=1)
        field_label = show._meta.get_field('when_time').verbose_name
        self.assertEquals(field_label, 'when time')

    def test___str__(self):
        show = EntityShow.objects.get(id=1)
        expected_label = 'show'
        self.assertEquals(expected_label, str(show))

    def test_display_show_name_when_with_date_and_time(self):
        show = EntityShow.objects.get(id=1)
        expected_label = 'show, 1970-01-01, 01:00:00'
        self.assertEquals(expected_label, show.display_show_name_with_date_and_time())
        show = EntityShow.objects.get(id=2)
        expected_label = 'show, 1970-01-01'
        self.assertEquals(expected_label, show.display_show_name_with_date_and_time())


class EntityOrganityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        EntityOrganity.objects.create(name='venue')

    def test_name_label(self):
        venue = EntityOrganity.objects.get(id=1)
        field_label = venue._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test___str__(self):
        venue = EntityOrganity.objects.get(id=1)
        expected_label = 'venue'
        self.assertEquals(expected_label, str(venue))

    def test_get_absolute_url(self):
        venue = EntityOrganity.objects.get(id=1)
        self.assertEquals(venue.get_absolute_url(), '/catalog/organities/1')


class EntityProductionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        EntitySeason.objects.create(name='2015-2016', begin_date=datetime(2015,1,1), end_date=datetime(2015,12,31))
        EntityProduction.objects.create(name='production', season=EntitySeason.objects.get(id=1))

    def test_name_label(self):
        production = EntityProduction.objects.get(id=1)
        field_label = production._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test___str__(self):
        production = EntityProduction.objects.get(id=1)
        expected_label = 'production'
        self.assertEquals(expected_label, str(production))

    def test_display_name_and_season(self):
        production = EntityProduction.objects.get(id=1)
        expected_label = 'production (2015-2016)'
        self.assertEquals(expected_label, production.display_name_and_season())

    def test_get_absolute_url(self):
        production = EntityProduction.objects.get(id=1)
        self.assertEquals(production.get_absolute_url(), '/catalog/productions/1')

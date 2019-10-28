from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from datetime import datetime

from catalog.models import EntityShow, EntityVenue, EntityProduction, EntitySeason, EntityPerson


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


class EntityVenueModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        EntityVenue.objects.create(name='venue')

    def test_name_label(self):
        venue = EntityVenue.objects.get(id=1)
        field_label = venue._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test___str__(self):
        venue = EntityVenue.objects.get(id=1)
        expected_label = 'venue'
        self.assertEquals(expected_label, str(venue))

    def test_get_absolute_url(self):
        venue = EntityVenue.objects.get(id=1)
        self.assertEquals(venue.get_absolute_url(), '/catalog/venues/1')


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


class EntityPersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        EntityPerson.objects.create(first_name='tom', last_name='ruette', sort_name='ruette, tom', disambiguation='nerd')
        EntityPerson.objects.create(first_name='tom', sort_name='ruette, tom', disambiguation='nerd')
        EntityPerson.objects.create(last_name='ruette', sort_name='ruette, tom', disambiguation='nerd')
        EntityPerson.objects.create(sort_name='ruette, tom', disambiguation='nerd')
        EntityPerson.objects.create(sort_name='ruette, tom')

    def test_first_name_label(self):
        person = EntityPerson.objects.get(id=1)
        field_label = person._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        person = EntityPerson.objects.get(id=1)
        field_label = person._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_sort_name_label(self):
        person = EntityPerson.objects.get(id=1)
        field_label = person._meta.get_field('sort_name').verbose_name
        self.assertEquals(field_label, 'sort name')

    def test_disambiguation_label(self):
        person = EntityPerson.objects.get(id=1)
        field_label = person._meta.get_field('disambiguation').verbose_name
        self.assertEquals(field_label, 'disambiguation')

    def test___str__(self):
        person = EntityPerson.objects.get(id=1)
        expected_label = 'tom ruette'
        self.assertEquals(expected_label, person.display_full_name())

        person = EntityPerson.objects.get(id=2)
        expected_label = 'tom'
        self.assertEquals(expected_label, person.display_full_name())

        person = EntityPerson.objects.get(id=3)
        expected_label = 'ruette'
        self.assertEquals(expected_label, person.display_full_name())

        person = EntityPerson.objects.get(id=4)
        expected_label = 'ruette, tom'
        self.assertEquals(expected_label, person.display_full_name())

        person = EntityPerson.objects.get(id=5)
        expected_label = 'ruette, tom'
        self.assertEquals(expected_label, person.display_full_name())

    def test_display_full_name_and_disambiguation(self):
        person = EntityPerson.objects.get(id=1)
        expected_label = 'tom ruette (nerd)'
        self.assertEquals(expected_label, person.display_full_name_and_disambiguation())

        person = EntityPerson.objects.get(id=2)
        expected_label = 'tom (nerd)'
        self.assertEquals(expected_label, person.display_full_name_and_disambiguation())

        person = EntityPerson.objects.get(id=3)
        expected_label = 'ruette (nerd)'
        self.assertEquals(expected_label, person.display_full_name_and_disambiguation())

        person = EntityPerson.objects.get(id=4)
        expected_label = 'ruette, tom (nerd)'
        self.assertEquals(expected_label, person.display_full_name_and_disambiguation())

        person = EntityPerson.objects.get(id=5)
        expected_label = 'ruette, tom'
        self.assertEquals(expected_label, person.display_full_name_and_disambiguation())

    def test_get_absolute_url(self):
        person = EntityPerson.objects.get(id=1)
        self.assertEquals(person.get_absolute_url(), '/catalog/people/1')
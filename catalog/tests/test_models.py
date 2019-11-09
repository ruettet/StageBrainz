from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from datetime import datetime
from partial_date import PartialDate

from catalog.models import EntityShow, EntityProduction, Season, EntityOrganity, EntityCharacter
from catalog.models import RelationShowShow, RelationShowShowType, RelationProductionOrganity


class EntityShowModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        EntityShow.objects.create(name='show', when_date=PartialDate(datetime(1970, 1, 1, 1, 0, 0).date()), when_time=datetime(1970, 1, 1, 1, 0, 0).time())
        EntityShow.objects.create(name='show', when_date=PartialDate(datetime(1970, 1, 1, 1, 0, 0).date()))

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
        Season.objects.create(name='2015-2016', begin_date=PartialDate(datetime(2015, 1, 1)), end_date=PartialDate(datetime(2015, 12, 31)))
        EntityProduction.objects.create(name='production', season=Season.objects.get(id=1))

    def test_name_label(self):
        production = EntityProduction.objects.get(id=1)
        field_label = production._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test___str__(self):
        production = EntityProduction.objects.get(id=1)
        expected_label = 'production'
        self.assertEquals(expected_label, str(production))

    def test_get_absolute_url(self):
        production = EntityProduction.objects.get(id=1)
        self.assertEquals(production.get_absolute_url(), '/catalog/productions/1')


class RelationShowShowTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        show_a = EntityShow.objects.create(name='show_a', when_date=PartialDate(datetime(2016, 1, 1)))
        show_a.save()
        show_b = EntityShow.objects.create(name='show_b', when_date=PartialDate(datetime(2017, 1, 1)))
        show_b.save()
        rss_with_relation_with_relation_name = RelationShowShow.objects.create(entity_a=show_a, entity_b=show_b, relation_name="test_name")
        rss_with_relation_with_relation_name.relation_type.create(name='test', inverted_name='inverted test')
        rss_without_relation_with_relation_name = RelationShowShow.objects.create(entity_a=show_a, entity_b=show_b, relation_name="test_name")
        rss_with_relation_without_relation_name = RelationShowShow.objects.create(entity_a=show_a, entity_b=show_b)
        rss_with_relation_without_relation_name.relation_type.create(name='test', inverted_name='inverted test')
        rss_without_relation_without_relation_name = RelationShowShow.objects.create(entity_a=show_a, entity_b=show_b)
        inverted_rss_with_relation_without_relation_name = RelationShowShow.objects.create(entity_a=show_a, entity_b=show_b, inverted_relation=True)
        inverted_rss_with_relation_without_relation_name.relation_type.create(name='test', inverted_name='inverted test')
        rss_with_relation_with_relation_name.save()
        rss_without_relation_with_relation_name.save()
        rss_with_relation_without_relation_name.save()
        rss_without_relation_without_relation_name.save()
        inverted_rss_with_relation_without_relation_name.save()

    def test_entity_names(self):
        rss = RelationShowShow.objects.get(id=1)
        self.assertEquals(rss.entity_a.name, 'show_a')
        self.assertEquals(rss.entity_b.name, 'show_b')

    def test_relation_type_relation_name(self):
        rss = RelationShowShow.objects.get(id=1)
        self.assertEquals(rss.display_relation_name(), 'test_name')

    def test_relation_type_name(self):
        rss = RelationShowShow.objects.get(id=3)
        self.assertEquals(rss.display_relation_name(), 'test')

    def test_relation_name_with_relation_with_name(self):
        rss = RelationShowShow.objects.get(id=1)
        self.assertEquals(str(rss), 'show_a <test_name> show_b')

    def test_relation_name_without_relation_with_name(self):
        rss = RelationShowShow.objects.get(id=2)
        self.assertEquals(str(rss), 'show_a <test_name> show_b')

    def test_relation_name_without_relation_without_name(self):
        rss = RelationShowShow.objects.get(id=3)
        self.assertEquals(str(rss), 'show_a <test> show_b')

    def test_relation_name_without_relation_without_name(self):
        rss = RelationShowShow.objects.get(id=4)
        self.assertEquals(str(rss), 'show_a <not set> show_b')

    def test_inverted_relation_name_with_relation_without_name(self):
        rss = RelationShowShow.objects.get(id=5)
        self.assertEquals(str(rss), 'show_b <inverted test> show_a')


class RelationProductionOrganityTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        char = EntityCharacter.objects.create(name="character")
        char.save()
        production = EntityProduction.objects.create(name='production')
        production.save()
        organity = EntityOrganity.objects.create(name='organity')
        organity.save()
        rel = RelationProductionOrganity.objects.create(entity_a=production, entity_b=organity, context_of_character=char)
        rel.save
        rel = RelationProductionOrganity.objects.create(entity_a=production, entity_b=organity, context_of_character=char, context_of_character_str="character_str")
        rel.save

    def test_display_context_of_character(self):
        rel = RelationProductionOrganity.objects.get(id=1)
        self.assertEquals(rel.display_context_of_character(), "character")

    def test_display_context_of_character(self):
        rel = RelationProductionOrganity.objects.get(id=2)
        self.assertEquals(rel.display_context_of_character(), "character_str")

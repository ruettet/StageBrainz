from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


# Create your models here.
class EntityShow(models.Model):
    """Model representing a show, i.e. a performance of a Production"""
    name = models.CharField(max_length=200, help_text='Enter a name for the show')
    when_date = models.DateField()
    when_time = models.TimeField(blank=True, null=True)
    show_type = models.ManyToManyField('EntityShowType', blank=True)

    def __str__(self):
        """"String for representing the model object"""
        return self.name

    def display_show_name_with_date_and_time(self):
        output = self.name + ", " + self.display_show_when()
        return output

    def display_show_when(self):
        date_iso = self.when_date.isoformat()
        return date_iso + ", " + self.when_time.isoformat() if self.when_time is not None else date_iso

    class Meta:
        ordering = ['-when_date', '-when_time']


class EntityShowType(models.Model):
    """Model representing show types, i.e. a premiere"""
    name = models.CharField(max_length=200, help_text='Enter a name for a show type')

    def __str__(self):
        return self.name


class EntityVenue(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a name for the venue')
    disambiguation = models.CharField(max_length=200, help_text='A Disambiguation Line', blank=True, null=True)
    venue_types = models.ManyToManyField('EntityVenueType', blank=True)

    def __str__(self):
        """"String for representing the model object"""
        return self.name

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this venue"""
        return reverse('venue-detail', args=[str(self.id)])


class EntityVenueType(models.Model):
    """"Model representing venue types, i.e. Theater, Arena, Outside"""
    name = models.CharField(max_length=200, help_text='Enter a name for a venue type')

    def __str__(self):
        return self.name


class EntityVenueAlias(models.Model):
    name = models.CharField(max_length=200, help_text='Enter an alias for the venue')
    venue = models.ForeignKey(EntityVenue, on_delete=models.PROTECT)
    alias_type = models.ForeignKey('EntityVenueAliasType', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class EntityVenueAliasType(models.Model):
    name = models.CharField(max_length=200, help_text='A venue alias type')

    def __str__(self):
        return self.name


class EntityProduction(models.Model):
    """"Model representing stage productions, which must be an instantiation of a work in a season"""
    name = models.CharField(max_length=200, help_text='Title of the stage production')
    disambiguation = models.CharField(max_length=200, help_text='A disambiguation line', blank=True, null=True)
    season = models.ForeignKey('EntitySeason', on_delete=models.PROTECT)
    production_type = models.ManyToManyField('EntityProductionType', blank=True)

    def __str__(self):
        return self.name

    def display_name_and_season(self):
        return str(self.name) + " (" + self.season.name + ")"

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this production"""
        return reverse('productions-detail', args=[str(self.id)])


class EntityProductionType(models.Model):
    """"Model representing stage production types, e.g. """
    name = models.CharField(max_length=200, help_text='Enter a name for a production type')

    def __str__(self):
        return self.name


class EntitySeason(models.Model):
    """"Model representing a traditional season"""
    name = models.CharField(max_length=200, help_text='Enter a name for the season')
    begin_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class EntityPerson(models.Model):
    first_name = models.CharField(max_length=200, help_text='First name of a person', blank=True, null=True)
    last_name = models.CharField(max_length=200, help_text='Last name of a person', blank=True, null=True)
    sort_name = models.CharField(max_length=200, help_text='Representation of the name to sort on', default='please provide a sort name')
    disambiguation = models.CharField(max_length=200, help_text='Some disambiguation information', blank=True, null=True)
    person_type = models.ManyToManyField('EntityPersonType', blank=True)

    def __str__(self):
        return self.sort_name

    def display_full_name(self):
        str_first_name = self.first_name if self.first_name is not None else ''
        str_last_name = self.last_name if self.last_name is not None else ''
        full_name = str_first_name + ' ' + str_last_name
        full_name = full_name.strip()
        return full_name if len(full_name) > 0 else self.sort_name

    def display_full_name_and_disambiguation(self):
        str_disambiguation = ' (' + self.disambiguation + ')' if self.disambiguation is not None else ''
        return self.display_full_name() + str_disambiguation

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this production"""
        return reverse('people-detail', args=[str(self.id)])


class EntityPersonType(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a name for a person type')

    def __str__(self):
        return self.name


class EntityPersonAlias(models.Model):
    name = models.CharField(max_length=200, help_text='Enter an alias for the person')
    person = models.ForeignKey(EntityPerson, on_delete=models.PROTECT)
    alias_type = models.ForeignKey('EntityPersonAliasType', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class EntityPersonAliasType(models.Model):
    name = models.CharField(max_length=200, help_text='A person alias type')

    def __str__(self):
        return self.name


class EntityOrganisation(models.Model):
    name = models.CharField(max_length=200, help_text='Name of an organisation')
    sort_name = models.CharField(max_length=200, help_text='Sort on this name', default='not yet set')
    disambiguation = models.CharField(max_length=200, help_text='A disambiguation line', blank=True, null=True)
    organisation_type = models.ManyToManyField('EntityOrganisationType', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this production"""
        return reverse('organisations-detail', args=[str(self.id)])


class EntityOrganisationType(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a name for an organisation type')

    def __str__(self):
        return self.name


class EntityOrganisationAlias(models.Model):
    name = models.CharField(max_length=200, help_text='Enter an alias for the organisation')
    organisation = models.ForeignKey(EntityOrganisation, on_delete=models.PROTECT)
    alias_type = models.ForeignKey('EntityOrganisationAliasType', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class EntityOrganisationAliasType(models.Model):
    name = models.CharField(max_length=200, help_text='An organisation alias type')

    def __str__(self):
        return self.name


class EntityWork(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a name for the work')
    disambiguation = models.CharField(max_length=200, help_text='A Disambiguation Line', blank=True, null=True)
    work_type = models.ManyToManyField('EntityWorkType', blank=True)

    def __str__(self):
        """"String for representing the model object"""
        return self.name

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this venue"""
        return reverse('work-detail', args=[str(self.id)])


class EntityWorkType(models.Model):
    """"Model representing work types, i.e. Theatertext, Novel"""
    name = models.CharField(max_length=200, help_text='Enter a name for a work type')

    def __str__(self):
        return self.name


class EntityWorkAlias(models.Model):
    name = models.CharField(max_length=200, help_text='Enter an alias for the work')
    work = models.ForeignKey(EntityWork, on_delete=models.PROTECT)
    alias_type = models.ForeignKey('EntityWorkAliasType', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class EntityWorkAliasType(models.Model):
    name = models.CharField(max_length=200, help_text='A work alias type')

    def __str__(self):
        return self.name


class EntityCharacter(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a name for the character')
    disambiguation = models.CharField(max_length=200, help_text='A disambiguation line', blank=True, null=True)
    character_type = models.ManyToManyField('EntityCharacterType', blank=True)

    def __str__(self):
        """"String for representing the model object"""
        return self.name

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this character"""
        return reverse('character-detail', args=[str(self.id)])


class EntityCharacterType(models.Model):
    """"Model representing work types, i.e. Theatertext, Novel"""
    name = models.CharField(max_length=200, help_text='Enter a name for a character type')

    def __str__(self):
        return self.name


class EntityCharacterAlias(models.Model):
    name = models.CharField(max_length=200, help_text='Enter an alias for the character')
    character = models.ForeignKey(EntityCharacter, on_delete=models.PROTECT)
    alias_type = models.ForeignKey('EntityCharacterAliasType', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class EntityCharacterAliasType(models.Model):
    name = models.CharField(max_length=200, help_text='A character alias type')

    def __str__(self):
        return self.name


class EntityGenre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a name for the genre')
    genre_type = models.ManyToManyField('EntityGenreType', blank=True)

    def __str__(self):
        """"String for representing the model object"""
        return self.name

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this character"""
        return reverse('genre-detail', args=[str(self.id)])


class EntityGenreType(models.Model):
    """"Model representing work types, i.e. Theatertext, Novel"""
    name = models.CharField(max_length=200, help_text='Enter a name for a genre type')

    def __str__(self):
        return self.name


class EntityGenreAlias(models.Model):
    name = models.CharField(max_length=200, help_text='Enter an alias for the genre')
    genre = models.ForeignKey(EntityGenre, on_delete=models.PROTECT)
    alias_type = models.ForeignKey('EntityGenreAliasType', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class EntityGenreAliasType(models.Model):
    name = models.CharField(max_length=200, help_text='A genre alias type')

    def __str__(self):
        return self.name


class EntityUrl(models.Model):
    """Model representing a show, i.e. a performance of a Production"""
    href = models.CharField(max_length=200, help_text='Enter the url')
    name = models.CharField(max_length=200, help_text='Enter a name for the url', blank=True, null=True)
    url_type = models.ManyToManyField('EntityUrlType', blank=True)

    def __str__(self):
        """"String for representing the model object"""
        return self.name

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this show"""
        return reverse('url-detail', args=[str(self.id)])


class EntityUrlType(models.Model):
    """Model representing show types, i.e. a premiere"""
    name = models.CharField(max_length=200, help_text='Enter a name for a url type')

    def __str__(self):
        return self.name


# Relations
class RelationShowShow(models.Model):
    show_a = models.ForeignKey(EntityShow, on_delete=models.PROTECT, related_name='%(class)s_show_a')
    show_a_name = models.CharField(max_length=200, help_text='If first show was credited differently', blank=True, null=True)
    show_b = models.ForeignKey(EntityShow, on_delete=models.PROTECT, related_name='%(class)s_show_b')
    show_b_name = models.CharField(max_length=200, help_text='If second show was credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')
    relation_type = models.ForeignKey('RelationShowShowType', on_delete=models.PROTECT)

    def __str__(self):
        return self.show_a.name + ' <' + str(self.relation_type.name) + '>' + self.show_b.name


class RelationShowShowType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the show - show relation type')

    def __str__(self):
        return self.name


class RelationShowVenue(models.Model):
    show = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    show_name = models.CharField(max_length=200, help_text='If show was credited differently', blank=True, null=True)
    venue = models.ForeignKey('EntityVenue', on_delete=models.PROTECT)
    venue_name = models.CharField(max_length=200, help_text='If venue was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationShowVenueType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_show_name = self.display_show_name()
        str_venue_name = self.display_venue_name()
        str_show_when = self.show.display_show_when()
        return str_show_name + ' <' + str(self.relation_type.name) + '> ' + str_venue_name + ', ' + str_show_when

    def display_show_name(self):
        return self.show.name if self.show_name is None else self.show_name

    def display_venue_name(self):
        return self.venue.name if self.venue_name is None else self.venue_name

    def display_show_when(self):
        return self.show.display_show_when()


class RelationShowVenueType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the show - venue relation type')

    def __str__(self):
        return self.name


class RelationShowProduction(models.Model):
    show = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    show_name = models.CharField(max_length=200, help_text='If show was credited differently', blank=True, null=True)
    production = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    production_name = models.CharField(max_length=200, help_text='If production was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationShowProductionType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_show_name = self.display_show_name()
        str_production_name = self.display_production_name()
        str_show_when = self.show.display_show_when()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_show_name + ' <' + str_relation + '> ' + str_production_name + ', ' + str_show_when

    def display_show_name(self):
        return self.show.name if self.show_name is None else self.show_name

    def display_production_name(self):
        return self.production.name if self.production_name is None else self.production_name


class RelationShowProductionType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the show - production relation type')

    def __str__(self):
        return self.name


class RelationShowPerson(models.Model):
    show = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    show_name = models.CharField(max_length=200, help_text='If show was credited differently', blank=True, null=True)
    person = models.ForeignKey('EntityPerson', on_delete=models.PROTECT)
    person_name = models.CharField(max_length=200, help_text='If person was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationShowPersonType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_show_name = self.display_show_name()
        str_person_name = self.display_person_name()
        str_show_when = self.show.display_show_when()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_show_name + ' <' + str_relation + '> ' + str_person_name + ', ' + str_show_when

    def display_show_name(self):
        return self.show.name if self.show_name is None else self.show_name

    def display_person_name(self):
        return self.person.name if self.person_name is None else self.person_name


class RelationShowPersonType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the show - person relation type')

    def __str__(self):
        return self.name


class RelationShowOrganisation(models.Model):
    show = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    show_name = models.CharField(max_length=200, help_text='If show was credited differently', blank=True, null=True)
    organisation = models.ForeignKey('EntityOrganisation', on_delete=models.PROTECT)
    organisation_name = models.CharField(max_length=200, help_text='If person was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationShowOrganisationType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_show_name = self.display_show_name()
        str_organisation_name = self.display_organisation_name()
        str_show_when = self.show.display_show_when()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_show_name + ' <' + str_relation + '> ' + str_organisation_name + ', ' + str_show_when

    def display_show_name(self):
        return self.show.name if self.show_name is None else self.show_name

    def display_organisation_name(self):
        return self.organisation.name if self.organisation_name is None else self.organisation_name


class RelationShowOrganisationType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the show - organisation relation type')

    def __str__(self):
        return self.name


class RelationShowWork(models.Model):
    show = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    show_name = models.CharField(max_length=200, help_text='If show was credited differently', blank=True, null=True)
    work = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    work_name = models.CharField(max_length=200, help_text='If work was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationShowWorkType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_show_name = self.display_show_name()
        str_work_name = self.display_work_name()
        str_show_when = self.show.display_show_when()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_show_name + ' <' + str_relation + '> ' + str_work_name + ', ' + str_show_when

    def display_show_name(self):
        return self.show.name if self.show_name is None else self.show_name

    def display_work_name(self):
        return self.work.name if self.work_name is None else self.work_name


class RelationShowWorkType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the show - work relation type')

    def __str__(self):
        return self.name


class RelationShowCharacter(models.Model):
    show = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    show_name = models.CharField(max_length=200, help_text='If show was credited differently', blank=True, null=True)
    character = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    character_name = models.CharField(max_length=200, help_text='If character was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationShowCharacterType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_show_name = self.display_show_name()
        str_character_name = self.display_character_name()
        str_show_when = self.show.display_show_when()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_show_name + ' <' + str_relation + '> ' + str_character_name + ', ' + str_show_when

    def display_show_name(self):
        return self.show.name if self.show_name is None else self.show_name

    def display_character_name(self):
        return self.character.name if self.character_name is None else self.character_name


class RelationShowCharacterType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the show - character relation type')

    def __str__(self):
        return self.name


class RelationShowGenre(models.Model):
    show = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    show_name = models.CharField(max_length=200, help_text='If show was credited differently', blank=True, null=True)
    genre = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    genre_name = models.CharField(max_length=200, help_text='If genre was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationShowGenreType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_show_name = self.display_show_name()
        str_genre_name = self.display_genre_name()
        str_show_when = self.show.display_show_when()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_show_name + ' <' + str_relation + '> ' + str_genre_name + ', ' + str_show_when

    def display_show_name(self):
        return self.show.name if self.show_name is None else self.show_name

    def display_genre_name(self):
        return self.genre.name if self.genre_name is None else self.genre_name


class RelationShowGenreType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the show - genre relation type')

    def __str__(self):
        return self.name


class RelationShowUrl(models.Model):
    show = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    show_name = models.CharField(max_length=200, help_text='If show was credited differently', blank=True, null=True)
    url = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    url_name = models.CharField(max_length=200, help_text='If url was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationShowUrlType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_show_name = self.display_show_name()
        str_url_name = self.display_url_name()
        str_show_when = self.show.display_show_when()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_show_name + ' <' + str_relation + '> ' + str_url_name + ', ' + str_show_when

    def display_show_name(self):
        return self.show.name if self.show_name is None else self.show_name

    def display_url_name(self):
        return self.url.name if self.url_name is None else self.url_name


class RelationShowUrlType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the show - url relation type')

    def __str__(self):
        return self.name


class RelationVenueVenue(models.Model):
    venue_a = models.ForeignKey(EntityVenue, on_delete=models.PROTECT, related_name='%(class)s_venue_a')
    venue_a_name = models.CharField(max_length=200, help_text='If first venue was credited differently', blank=True, null=True)
    venue_b = models.ForeignKey(EntityVenue, on_delete=models.PROTECT, related_name='%(class)s_venue_b')
    venue_b_name = models.CharField(max_length=200, help_text='If second venue was credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')
    relation_type = models.ForeignKey('RelationVenueVenueType', on_delete=models.PROTECT)

    def __str__(self):
        return self.venue_a.name + ' <' + str(self.relation_type.name) + '>' + self.venue_b.name


class RelationVenueVenueType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the show - show relation type')

    def __str__(self):
        return self.name


class RelationVenueProduction(models.Model):
    venue = models.ForeignKey('EntityVenue', on_delete=models.PROTECT)
    venue_name = models.CharField(max_length=200, help_text='If venue was credited differently', blank=True, null=True)
    production = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    production_name = models.CharField(max_length=200, help_text='If production was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationVenueProductionType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_venue_name = self.display_venue_name()
        str_production_name = self.display_production_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_venue_name + ' <' + str_relation + '> ' + str_production_name

    def display_venue_name(self):
        return self.venue.name if self.venue_name is None else self.venue_name

    def display_production_name(self):
        return self.production.name if self.production_name is None else self.production_name


class RelationVenueProductionType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the venue - production relation type')

    def __str__(self):
        return self.name


class RelationVenuePerson(models.Model):
    venue = models.ForeignKey('EntityVenue', on_delete=models.PROTECT)
    venue_name = models.CharField(max_length=200, help_text='If venue was credited differently', blank=True, null=True)
    person = models.ForeignKey('EntityPerson', on_delete=models.PROTECT)
    person_name = models.CharField(max_length=200, help_text='If person was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationVenuePersonType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_venue_name = self.display_venue_name()
        str_person_name = self.display_person_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_venue_name + ' <' + str_relation + '> ' + str_person_name

    def display_venue_name(self):
        return self.venue.name if self.venue_name is None else self.venue_name

    def display_person_name(self):
        return self.person.display_full_name() if self.person_name is None else self.person_name


class RelationVenuePersonType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the venue - person relation type')

    def __str__(self):
        return self.name


class RelationVenueOrganisation(models.Model):
    venue = models.ForeignKey('EntityVenue', on_delete=models.PROTECT)
    venue_name = models.CharField(max_length=200, help_text='If venue was credited differently', blank=True, null=True)
    organisation = models.ForeignKey('EntityOrganisation', on_delete=models.PROTECT)
    organisation_name = models.CharField(max_length=200, help_text='If organisation was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationVenueOrganisationType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_venue_name = self.display_venue_name()
        str_organisation_name = self.display_organisation_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_venue_name + ' <' + str_relation + '> ' + str_organisation_name

    def display_venue_name(self):
        return self.venue.name if self.venue_name is None else self.venue_name

    def display_organisation_name(self):
        return self.organisation.name if self.organisation_name is None else self.organisation_name


class RelationVenueOrganisationType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the venue - organisation relation type')

    def __str__(self):
        return self.name


class RelationVenueWork(models.Model):
    venue = models.ForeignKey('EntityVenue', on_delete=models.PROTECT)
    venue_name = models.CharField(max_length=200, help_text='If venue was credited differently', blank=True, null=True)
    work = models.ForeignKey('EntityOrganisation', on_delete=models.PROTECT)
    work_name = models.CharField(max_length=200, help_text='If work was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationVenueWorkType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_venue_name = self.display_venue_name()
        str_work_name = self.display_work_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_venue_name + ' <' + str_relation + '> ' + str_work_name

    def display_venue_name(self):
        return self.venue.name if self.venue_name is None else self.venue_name

    def display_work_name(self):
        return self.work.name if self.work_name is None else self.work_name


class RelationVenueWorkType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the venue - work relation type')

    def __str__(self):
        return self.name


class RelationVenueCharacter(models.Model):
    venue = models.ForeignKey('EntityVenue', on_delete=models.PROTECT)
    venue_name = models.CharField(max_length=200, help_text='If venue was credited differently', blank=True, null=True)
    character = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    character_name = models.CharField(max_length=200, help_text='If character was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationVenueCharacterType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_venue_name = self.display_venue_name()
        str_character_name = self.display_character_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_venue_name + ' <' + str_relation + '> ' + str_character_name

    def display_venue_name(self):
        return self.venue.name if self.venue_name is None else self.venue_name

    def display_character_name(self):
        return self.character.name if self.character_name is None else self.character_name


class RelationVenueCharacterType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the venue - character relation type')

    def __str__(self):
        return self.name


class RelationVenueGenre(models.Model):
    venue = models.ForeignKey('EntityVenue', on_delete=models.PROTECT)
    venue_name = models.CharField(max_length=200, help_text='If venue was credited differently', blank=True, null=True)
    genre = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    genre_name = models.CharField(max_length=200, help_text='If genre was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationVenueGenreType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_venue_name = self.display_venue_name()
        str_genre_name = self.display_genre_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_venue_name + ' <' + str_relation + '> ' + str_genre_name

    def display_venue_name(self):
        return self.venue.name if self.venue_name is None else self.venue_name

    def display_genre_name(self):
        return self.genre.name if self.genre_name is None else self.genre_name


class RelationVenueGenreType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the venue - genre relation type')

    def __str__(self):
        return self.name


class RelationVenueUrl(models.Model):
    venue = models.ForeignKey('EntityVenue', on_delete=models.PROTECT)
    venue_name = models.CharField(max_length=200, help_text='If venue was credited differently', blank=True, null=True)
    url = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    url_name = models.CharField(max_length=200, help_text='If url was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationVenueUrlType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_venue_name = self.display_venue_name()
        str_url_name = self.display_url_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_venue_name + ' <' + str_relation + '> ' + str_url_name

    def display_venue_name(self):
        return self.venue.name if self.venue_name is None else self.venue_name

    def display_url_name(self):
        return self.url.name if self.url_name is None else self.url_name


class RelationVenueUrlType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the venue - url relation type')

    def __str__(self):
        return self.name


class RelationProductionProduction(models.Model):
    production_a = models.ForeignKey(EntityProduction, on_delete=models.PROTECT, related_name='%(class)s_production_a')
    production_a_name = models.CharField(max_length=200, help_text='If first production was credited differently', blank=True, null=True)
    production_b = models.ForeignKey(EntityProduction, on_delete=models.PROTECT, related_name='%(class)s_production_b')
    production_b_name = models.CharField(max_length=200, help_text='If second production was credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')
    relation_type = models.ForeignKey('RelationProductionProductionType', on_delete=models.PROTECT)

    def __str__(self):
        return self.production_a.name + ' <' + str(self.relation_type.name) + '>' + self.production_b.name


class RelationProductionProductionType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the production - production relation type')

    def __str__(self):
        return self.name


class RelationProductionPerson(models.Model):
    production = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    production_name = models.CharField(max_length=200, help_text='If production was credited differently', blank=True, null=True)
    person = models.ForeignKey('EntityPerson', on_delete=models.PROTECT)
    person_name = models.CharField(max_length=200, help_text='If person was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationProductionPersonType', on_delete=models.PROTECT)
    relation_str = models.CharField(max_length=200, help_text='If relation is credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_production_name = self.display_production_name()
        str_person_name = self.display_person_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_production_name + ' <' + str_relation + '> ' + str_person_name

    def display_production_name(self):
        return self.production.name if self.production_name is None else self.production_name

    def display_person_name(self):
        return self.person.display_full_name() if self.person_name is None else self.person_name


class RelationProductionPersonType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the production - person relation type')

    def __str__(self):
        return self.name


class RelationProductionOrganisation(models.Model):
    production = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    production_name = models.CharField(max_length=200, help_text='If production was credited differently', blank=True, null=True)
    organisation = models.ForeignKey('EntityOrganisation', on_delete=models.PROTECT)
    organisation_name = models.CharField(max_length=200, help_text='If organisation was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationProductionOrganisationType', on_delete=models.PROTECT)
    relation_str = models.CharField(max_length=200, help_text='If relation is credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_production_name = self.display_production_name()
        str_organisation_name = self.display_organisation_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_production_name + ' <' + str_relation + '> ' + str_organisation_name

    def display_production_name(self):
        return self.production.name if self.production_name is None else self.production_name

    def display_organisation_name(self):
        return self.organisation.name if self.organisation_name is None else self.organisation_name


class RelationProductionOrganisationType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the production - organisation relation type')

    def __str__(self):
        return self.name


class RelationProductionWork(models.Model):
    production = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    production_name = models.CharField(max_length=200, help_text='If production was credited differently', blank=True, null=True)
    work = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    work_name = models.CharField(max_length=200, help_text='If work was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationProductionWorkType', on_delete=models.PROTECT)
    relation_str = models.CharField(max_length=200, help_text='If relation is credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_production_name = self.display_production_name()
        str_work_name = self.display_work_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_production_name + ' <' + str_relation + '> ' + str_work_name

    def display_production_name(self):
        return self.production.name if self.production_name is None else self.production_name

    def display_work_name(self):
        return self.work.name if self.work_name is None else self.work_name


class RelationProductionWorkType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the production - work relation type')

    def __str__(self):
        return self.name


class RelationProductionCharacter(models.Model):
    production = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    production_name = models.CharField(max_length=200, help_text='If production was credited differently', blank=True, null=True)
    character = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    character_name = models.CharField(max_length=200, help_text='If character was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationProductionCharacterType', on_delete=models.PROTECT)
    relation_str = models.CharField(max_length=200, help_text='If relation is credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_production_name = self.display_production_name()
        str_character_name = self.display_character_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_production_name + ' <' + str_relation + '> ' + str_character_name

    def display_production_name(self):
        return self.production.name if self.production_name is None else self.production_name

    def display_character_name(self):
        return self.character.name if self.character_name is None else self.character_name


class RelationProductionCharacterType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the production - character relation type')

    def __str__(self):
        return self.name


class RelationProductionGenre(models.Model):
    production = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    production_name = models.CharField(max_length=200, help_text='If production was credited differently', blank=True, null=True)
    genre = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    genre_name = models.CharField(max_length=200, help_text='If genre was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationProductionGenreType', on_delete=models.PROTECT)
    relation_str = models.CharField(max_length=200, help_text='If relation is credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_production_name = self.display_production_name()
        str_genre_name = self.display_genre_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_production_name + ' <' + str_relation + '> ' + str_genre_name

    def display_production_name(self):
        return self.production.name if self.production_name is None else self.production_name

    def display_genre_name(self):
        return self.genre.name if self.genre_name is None else self.genre_name


class RelationProductionGenreType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the production - genre relation type')

    def __str__(self):
        return self.name


class RelationProductionUrl(models.Model):
    production = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    production_name = models.CharField(max_length=200, help_text='If production was credited differently', blank=True, null=True)
    url = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    url_name = models.CharField(max_length=200, help_text='If url was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationProductionUrlType', on_delete=models.PROTECT)
    relation_str = models.CharField(max_length=200, help_text='If relation is credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_production_name = self.display_production_name()
        str_url_name = self.display_url_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_production_name + ' <' + str_relation + '> ' + str_url_name

    def display_production_name(self):
        return self.production.name if self.production_name is None else self.production_name

    def display_url_name(self):
        return self.url.name if self.url_name is None else self.url_name


class RelationProductionUrlType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the production - url relation type')

    def __str__(self):
        return self.name

class RelationPersonPerson(models.Model):
    person_a = models.ForeignKey(EntityPerson, on_delete=models.PROTECT, related_name='%(class)s_person_a')
    person_a_name = models.CharField(max_length=200, help_text='If first person was credited differently', blank=True, null=True)
    person_b = models.ForeignKey(EntityPerson, on_delete=models.PROTECT, related_name='%(class)s_person_b')
    person_b_name = models.CharField(max_length=200, help_text='If second person was credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')
    relation_type = models.ForeignKey('RelationPersonPersonType', on_delete=models.PROTECT)

    def __str__(self):
        return self.person_a.display_full_name() + ' <' + str(self.relation_type.name) + '> ' + self.person_b.display_full_name()


class RelationPersonPersonType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the person - person relation type')

    def __str__(self):
        return self.name


class RelationPersonOrganisation(models.Model):
    person = models.ForeignKey('EntityPerson', on_delete=models.PROTECT)
    person_name = models.CharField(max_length=200, help_text='If person was credited differently', blank=True, null=True)
    organisation = models.ForeignKey('EntityOrganisation', on_delete=models.PROTECT)
    organisation_name = models.CharField(max_length=200, help_text='If organisation was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationPersonOrganisationType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_person_name = self.display_person_name()
        str_organisation_name = self.display_organisation_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_person_name + ' <' + str_relation + '> ' + str_organisation_name

    def display_person_name(self):
        return self.person.display_full_name() if self.person_name is None else self.person_name

    def display_organisation_name(self):
        return self.organisation.name if self.organisation_name is None else self.organisation_name


class RelationPersonOrganisationType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the person - organisation relation type')

    def __str__(self):
        return self.name


class RelationPersonWork(models.Model):
    person = models.ForeignKey('EntityPerson', on_delete=models.PROTECT)
    person_name = models.CharField(max_length=200, help_text='If person was credited differently', blank=True, null=True)
    work = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    work_name = models.CharField(max_length=200, help_text='If work was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationPersonWorkType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_person_name = self.display_person_name()
        str_work_name = self.display_work_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_person_name + ' <' + str_relation + '> ' + str_work_name

    def display_person_name(self):
        return self.person.display_full_name() if self.person_name is None else self.person_name

    def display_work_name(self):
        return self.work.name if self.work_name is None else self.work_name


class RelationPersonWorkType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the person - work relation type')

    def __str__(self):
        return self.name


class RelationPersonCharacter(models.Model):
    person = models.ForeignKey('EntityPerson', on_delete=models.PROTECT)
    person_name = models.CharField(max_length=200, help_text='If person was credited differently', blank=True, null=True)
    character = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    character_name = models.CharField(max_length=200, help_text='If character was credited differently', blank=True, null=True)
    production = models.ForeignKey('EntityProduction', on_delete=models.PROTECT, blank=True, null=True)
    production_name = models.CharField(max_length=200, help_text='When production is credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationPersonCharacterType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_person_name = self.display_person_name()
        str_character_name = self.display_character_name()
        str_production_name = self.display_production_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        production_info = ' in ' + str_production_name if str_production_name is not None else ''
        return str_person_name + ' <' + str_relation + '> ' + str_character_name + production_info

    def display_person_name(self):
        return self.person.display_full_name() if self.person_name is None else self.person_name

    def display_production_name(self):
        if self.production_name is None and self.production is None:
            return None
        else:
            return self.production.name if self.production_name is None else self.production_name

    def display_character_name(self):
        return self.character.name if self.character_name is None else self.character_name


class RelationPersonCharacterType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the person - character relation type')

    def __str__(self):
        return self.name


class RelationPersonGenre(models.Model):
    person = models.ForeignKey('EntityPerson', on_delete=models.PROTECT)
    person_name = models.CharField(max_length=200, help_text='If person was credited differently', blank=True, null=True)
    genre = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    genre_name = models.CharField(max_length=200, help_text='If genre was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationPersonGenreType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_person_name = self.display_person_name()
        str_genre_name = self.display_genre_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_person_name + ' <' + str_relation + '> ' + str_genre_name

    def display_person_name(self):
        return self.person.display_full_name() if self.person_name is None else self.person_name

    def display_genre_name(self):
        return self.genre.name if self.genre_name is None else self.genre_name


class RelationPersonGenreType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the person - genre relation type')

    def __str__(self):
        return self.name


class RelationPersonUrl(models.Model):
    person = models.ForeignKey('EntityPerson', on_delete=models.PROTECT)
    person_name = models.CharField(max_length=200, help_text='If person was credited differently', blank=True, null=True)
    url = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    url_name = models.CharField(max_length=200, help_text='If url was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationPersonUrlType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_person_name = self.display_person_name()
        str_url_name = self.display_url_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_person_name + ' <' + str_relation + '> ' + str_url_name

    def display_person_name(self):
        return self.person.display_full_name() if self.person_name is None else self.person_name

    def display_url_name(self):
        return self.url.name if self.url_name is None else self.url_name


class RelationPersonUrlType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the person - url relation type')

    def __str__(self):
        return self.name


class RelationOrganisationOrganisation(models.Model):
    organisation_a = models.ForeignKey(EntityOrganisation, on_delete=models.PROTECT, related_name='%(class)s_organisation_a')
    organisation_a_name = models.CharField(max_length=200, help_text='If first organisation was credited differently', blank=True, null=True)
    organisation_b = models.ForeignKey(EntityOrganisation, on_delete=models.PROTECT, related_name='%(class)s_organisation_b')
    organisation_b_name = models.CharField(max_length=200, help_text='If second organisation was credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')
    relation_type = models.ForeignKey('RelationOrganisationOrganisationType', on_delete=models.PROTECT)

    def __str__(self):
        return self.organisation_a.name + ' <' + str(self.relation_type.name) + '> ' + self.organisation_b.name


class RelationOrganisationOrganisationType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the organisation - organisation relation type')

    def __str__(self):
        return self.name


class RelationOrganisationWork(models.Model):
    organisation = models.ForeignKey('EntityOrganisation', on_delete=models.PROTECT)
    organisation_name = models.CharField(max_length=200, help_text='If organisation was credited differently', blank=True, null=True)
    work = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    work_name = models.CharField(max_length=200, help_text='If work was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationOrganisationWorkType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_organisation_name = self.display_organisation_name()
        str_work_name = self.display_work_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_organisation_name + ' <' + str_relation + '> ' + str_work_name

    def display_organisation_name(self):
        return self.organisation.name if self.organisation_name is None else self.organisation_name

    def display_work_name(self):
        return self.work.name if self.work_name is None else self.work_name


class RelationOrganisationWorkType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the organisation - work relation type')

    def __str__(self):
        return self.name


class RelationOrganisationCharacter(models.Model):
    organisation = models.ForeignKey('EntityOrganisation', on_delete=models.PROTECT)
    organisation_name = models.CharField(max_length=200, help_text='If organisation was credited differently', blank=True, null=True)
    character = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    character_name = models.CharField(max_length=200, help_text='If character was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationOrganisationCharacterType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_organisation_name = self.display_organisation_name()
        str_character_name = self.display_character_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_organisation_name + ' <' + str_relation + '> ' + str_character_name

    def display_organisation_name(self):
        return self.organisation.name if self.organisation_name is None else self.organisation_name

    def display_character_name(self):
        return self.character.name if self.character_name is None else self.character_name


class RelationOrganisationCharacterType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the organisation - character relation type')

    def __str__(self):
        return self.name


class RelationOrganisationGenre(models.Model):
    organisation = models.ForeignKey('EntityOrganisation', on_delete=models.PROTECT)
    organisation_name = models.CharField(max_length=200, help_text='If organisation was credited differently', blank=True, null=True)
    genre = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    genre_name = models.CharField(max_length=200, help_text='If genre was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationOrganisationGenreType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_organisation_name = self.display_organisation_name()
        str_genre_name = self.display_genre_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_organisation_name + ' <' + str_relation + '> ' + str_genre_name

    def display_organisation_name(self):
        return self.organisation.name if self.organisation_name is None else self.organisation_name

    def display_genre_name(self):
        return self.genre.name if self.genre_name is None else self.genre_name


class RelationOrganisationGenreType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the organisation - genre relation type')

    def __str__(self):
        return self.name


class RelationOrganisationUrl(models.Model):
    organisation = models.ForeignKey('EntityOrganisation', on_delete=models.PROTECT)
    organisation_name = models.CharField(max_length=200, help_text='If organisation was credited differently', blank=True, null=True)
    url = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    genre_name = models.CharField(max_length=200, help_text='If url was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationOrganisationUrlType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_organisation_name = self.display_organisation_name()
        str_url_name = self.display_url_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_organisation_name + ' <' + str_relation + '> ' + str_url_name

    def display_organisation_name(self):
        return self.organisation.name if self.organisation_name is None else self.organisation_name

    def display_url_name(self):
        return self.url.name if self.genre_name is None else self.genre_name


class RelationOrganisationUrlType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the organisation - url relation type')

    def __str__(self):
        return self.name


class RelationWorkWork(models.Model):
    work_a = models.ForeignKey(EntityWork, on_delete=models.PROTECT, related_name='%(class)s_work_a')
    work_a_name = models.CharField(max_length=200, help_text='If first work was credited differently', blank=True, null=True)
    work_b = models.ForeignKey(EntityWork, on_delete=models.PROTECT, related_name='%(class)s_work_b')
    work_b_name = models.CharField(max_length=200, help_text='If second work was credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')
    relation_type = models.ForeignKey('RelationWorkWorkType', on_delete=models.PROTECT)

    def __str__(self):
        return self.work_a.name + ' <' + str(self.relation_type.name) + '> ' + self.work_b.name


class RelationWorkWorkType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the work - work relation type')

    def __str__(self):
        return self.name


class RelationWorkCharacter(models.Model):
    work = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    work_name = models.CharField(max_length=200, help_text='If work was credited differently', blank=True, null=True)
    character = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    character_name = models.CharField(max_length=200, help_text='If character was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationWorkCharacterType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_work_name = self.display_work_name()
        str_character_name = self.display_character_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_work_name + ' <' + str_relation + '> ' + str_character_name

    def display_work_name(self):
        return self.work.name if self.work_name is None else self.work_name

    def display_character_name(self):
        return self.character.name if self.character_name is None else self.character_name


class RelationWorkCharacterType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the work - character relation type')

    def __str__(self):
        return self.name


class RelationWorkGenre(models.Model):
    work = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    work_name = models.CharField(max_length=200, help_text='If work was credited differently', blank=True, null=True)
    genre = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    genre_name = models.CharField(max_length=200, help_text='If genre was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationWorkGenreType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_work_name = self.display_work_name()
        str_genre_name = self.display_genre_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_work_name + ' <' + str_relation + '> ' + str_genre_name

    def display_work_name(self):
        return self.work.name if self.work_name is None else self.work_name

    def display_genre_name(self):
        return self.genre.name if self.genre_name is None else self.genre_name


class RelationWorkGenreType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the work - genre relation type')

    def __str__(self):
        return self.name


class RelationWorkUrl(models.Model):
    work = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    work_name = models.CharField(max_length=200, help_text='If work was credited differently', blank=True, null=True)
    url = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    url_name = models.CharField(max_length=200, help_text='If url was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationWorkUrlType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_work_name = self.display_work_name()
        str_url_name = self.display_url_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_work_name + ' <' + str_relation + '> ' + str_url_name

    def display_work_name(self):
        return self.work.name if self.work_name is None else self.work_name

    def display_url_name(self):
        return self.url.name if self.url_name is None else self.url_name


class RelationWorkUrlType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the work - url relation type')

    def __str__(self):
        return self.name


class RelationCharacterCharacter(models.Model):
    character_a = models.ForeignKey(EntityCharacter, on_delete=models.PROTECT, related_name='%(class)s_character_a')
    character_a_name = models.CharField(max_length=200, help_text='If first character was credited differently', blank=True, null=True)
    character_b = models.ForeignKey(EntityCharacter, on_delete=models.PROTECT, related_name='%(class)s_character_b')
    character_b_name = models.CharField(max_length=200, help_text='If second character was credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')
    relation_type = models.ForeignKey('RelationCharacterCharacterType', on_delete=models.PROTECT)

    def __str__(self):
        return self.character_a.name + ' <' + str(self.relation_type.name) + '> ' + self.character_b.name


class RelationCharacterCharacterType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the character - character relation type')

    def __str__(self):
        return self.name


class RelationCharacterGenre(models.Model):
    character = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    character_name = models.CharField(max_length=200, help_text='If character was credited differently', blank=True, null=True)
    genre = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    genre_name = models.CharField(max_length=200, help_text='If genre was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationCharacterGenreType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_character_name = self.display_character_name()
        str_genre_name = self.display_genre_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_character_name + ' <' + str_relation + '> ' + str_genre_name

    def display_character_name(self):
        return self.character.name if self.character_name is None else self.character_name

    def display_genre_name(self):
        return self.genre.name if self.genre_name is None else self.genre_name


class RelationCharacterGenreType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the character - genre relation type')

    def __str__(self):
        return self.name


class RelationCharacterUrl(models.Model):
    character = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    character_name = models.CharField(max_length=200, help_text='If character was credited differently', blank=True, null=True)
    url = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    url_name = models.CharField(max_length=200, help_text='If url was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationCharacterUrlType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_character_name = self.display_character_name()
        str_url_name = self.display_url_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_character_name + ' <' + str_relation + '> ' + str_url_name

    def display_character_name(self):
        return self.character.name if self.character_name is None else self.character_name

    def display_url_name(self):
        return self.url.name if self.url_name is None else self.url_name


class RelationCharacterUrlType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the character - url relation type')

    def __str__(self):
        return self.name


class RelationGenreGenre(models.Model):
    genre_a = models.ForeignKey(EntityGenre, on_delete=models.PROTECT, related_name='%(class)s_genre_a')
    genre_a_name = models.CharField(max_length=200, help_text='If first genre was credited differently', blank=True, null=True)
    genre_b = models.ForeignKey(EntityGenre, on_delete=models.PROTECT, related_name='%(class)s_genre_b')
    genre_b_name = models.CharField(max_length=200, help_text='If second genre was credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')
    relation_type = models.ForeignKey('RelationGenreGenreType', on_delete=models.PROTECT)

    def __str__(self):
        return self.genre_a.name + ' <' + str(self.relation_type.name) + '> ' + self.genre_b.name


class RelationGenreGenreType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the genre - genre relation type')

    def __str__(self):
        return self.name


class RelationGenreUrl(models.Model):
    genre = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    genre_name = models.CharField(max_length=200, help_text='If genre was credited differently', blank=True, null=True)
    url = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    url_name = models.CharField(max_length=200, help_text='If url was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationGenreUrlType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_genre_name = self.display_genre_name()
        str_url_name = self.display_url_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_genre_name + ' <' + str_relation + '> ' + str_url_name

    def display_genre_name(self):
        return self.genre.name if self.genre_name is None else self.genre_name

    def display_url_name(self):
        return self.url.name if self.url_name is None else self.url_name


class RelationGenreUrlType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the genre - url relation type')

    def __str__(self):
        return self.name


class RelationUrlUrl(models.Model):
    url_a = models.ForeignKey(EntityUrl, on_delete=models.PROTECT, related_name='%(class)s_url_a')
    url_a_name = models.CharField(max_length=200, help_text='If first url was credited differently', blank=True, null=True)
    url_b = models.ForeignKey(EntityUrl, on_delete=models.PROTECT, related_name='%(class)s_url_b')
    url_b_name = models.CharField(max_length=200, help_text='If second url was credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')
    relation_type = models.ForeignKey('RelationUrlUrlType', on_delete=models.PROTECT)

    def __str__(self):
        return self.url_a.name + ' <' + str(self.relation_type.name) + '> ' + self.url_b.name


class RelationUrlUrlType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the url - url relation type')

    def __str__(self):
        return self.name
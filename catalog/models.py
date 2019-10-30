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


class EntityOrganity(models.Model):
    name = models.CharField(max_length=200, help_text='Name of an organity')
    sort_name = models.CharField(max_length=200, help_text='Sort on this name', default='not yet set')
    disambiguation = models.CharField(max_length=200, help_text='A disambiguation line', blank=True, null=True)
    organity_type = models.ManyToManyField('EntityOrganityType', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this production"""
        return reverse('organities-detail', args=[str(self.id)])


class EntityOrganityType(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a name for an organity type')

    def __str__(self):
        return self.name


class EntityOrganityAlias(models.Model):
    name = models.CharField(max_length=200, help_text='Enter an alias for the organity')
    organity = models.ForeignKey(EntityOrganity, on_delete=models.PROTECT)
    alias_type = models.ForeignKey('EntityOrganityAliasType', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class EntityOrganityAliasType(models.Model):
    name = models.CharField(max_length=200, help_text='An organity alias type')

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
class RelationType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the x - y relation type', default='relation type')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


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


class RelationShowShowType(RelationType):
    pass


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


class RelationShowProductionType(RelationType):
    pass


class RelationShowOrganity(models.Model):
    show = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    show_name = models.CharField(max_length=200, help_text='If show was credited differently', blank=True, null=True)
    organity = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    organity_name = models.CharField(max_length=200, help_text='If person was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationShowOrganityType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_show_name = self.display_show_name()
        str_organity_name = self.display_organity_name()
        str_show_when = self.show.display_show_when()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_show_name + ' <' + str_relation + '> ' + str_organity_name + ', ' + str_show_when

    def display_show_name(self):
        return self.show.name if self.show_name is None else self.show_name

    def display_organity_name(self):
        return self.organity.name if self.organity_name is None else self.organity_name


class RelationShowOrganityType(RelationType):
    pass

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


class RelationShowWorkType(RelationType):
    pass


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


class RelationShowCharacterType(RelationType):
    pass

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


class RelationShowGenreType(RelationType):
    pass

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


class RelationShowUrlType(RelationType):
    pass


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


class RelationProductionProductionType(RelationType):
    pass


class RelationProductionOrganity(models.Model):
    production = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    production_name = models.CharField(max_length=200, help_text='If production was credited differently', blank=True, null=True)
    organity = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    organity_name = models.CharField(max_length=200, help_text='If organity was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationProductionOrganityType', on_delete=models.PROTECT)
    relation_str = models.CharField(max_length=200, help_text='If relation is credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_production_name = self.display_production_name()
        str_organity_name = self.display_organity_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_production_name + ' <' + str_relation + '> ' + str_organity_name

    def display_production_name(self):
        return self.production.name if self.production_name is None else self.production_name

    def display_organity_name(self):
        return self.organity.name if self.organity_name is None else self.organity_name


class RelationProductionOrganityType(RelationType):
    pass


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


class RelationProductionWorkType(RelationType):
    pass


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


class RelationProductionCharacterType(RelationType):
    pass


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


class RelationProductionGenreType(RelationType):
    pass


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


class RelationProductionUrlType(RelationType):
    pass


class RelationOrganityOrganity(models.Model):
    organity_a = models.ForeignKey(EntityOrganity, on_delete=models.PROTECT, related_name='%(class)s_organity_a')
    organity_a_name = models.CharField(max_length=200, help_text='If first organity was credited differently', blank=True, null=True)
    organity_b = models.ForeignKey(EntityOrganity, on_delete=models.PROTECT, related_name='%(class)s_organity_b')
    organity_b_name = models.CharField(max_length=200, help_text='If second organity was credited differently', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')
    relation_type = models.ForeignKey('RelationOrganityOrganityType', on_delete=models.PROTECT)

    def __str__(self):
        return self.organity_a.name + ' <' + str(self.relation_type.name) + '> ' + self.organity_b.name


class RelationOrganityOrganityType(RelationType):
    pass


class RelationOrganityWork(models.Model):
    organity = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    organity_name = models.CharField(max_length=200, help_text='If organity was credited differently', blank=True, null=True)
    work = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    work_name = models.CharField(max_length=200, help_text='If work was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationOrganityWorkType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_organity_name = self.display_organity_name()
        str_work_name = self.display_work_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_organity_name + ' <' + str_relation + '> ' + str_work_name

    def display_organity_name(self):
        return self.organity.name if self.organity_name is None else self.organity_name

    def display_work_name(self):
        return self.work.name if self.work_name is None else self.work_name


class RelationOrganityWorkType(RelationType):
    pass


class RelationOrganityCharacter(models.Model):
    organity = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    organity_name = models.CharField(max_length=200, help_text='If organity was credited differently', blank=True, null=True)
    character = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    character_name = models.CharField(max_length=200, help_text='If character was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationOrganityCharacterType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_organity_name = self.display_organity_name()
        str_character_name = self.display_character_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_organity_name + ' <' + str_relation + '> ' + str_character_name

    def display_organity_name(self):
        return self.organity.name if self.organity_name is None else self.organity_name

    def display_character_name(self):
        return self.character.name if self.character_name is None else self.character_name


class RelationOrganityCharacterType(RelationType):
    pass


class RelationOrganityGenre(models.Model):
    organity = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    organity_name = models.CharField(max_length=200, help_text='If organity was credited differently', blank=True, null=True)
    genre = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    genre_name = models.CharField(max_length=200, help_text='If genre was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationOrganityGenreType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_organity_name = self.display_organity_name()
        str_genre_name = self.display_genre_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_organity_name + ' <' + str_relation + '> ' + str_genre_name

    def display_organity_name(self):
        return self.organity.name if self.organity_name is None else self.organity_name

    def display_genre_name(self):
        return self.genre.name if self.genre_name is None else self.genre_name


class RelationOrganityGenreType(RelationType):
    pass


class RelationOrganityUrl(models.Model):
    organity = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    organity_name = models.CharField(max_length=200, help_text='If organity was credited differently', blank=True, null=True)
    url = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    genre_name = models.CharField(max_length=200, help_text='If url was credited differently', blank=True, null=True)
    relation_type = models.ForeignKey('RelationOrganityUrlType', on_delete=models.PROTECT)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')

    def __str__(self):
        str_organity_name = self.display_organity_name()
        str_url_name = self.display_url_name()
        str_relation = self.relation_type.name if self.relation_type.name is not None else 'not set'
        return str_organity_name + ' <' + str_relation + '> ' + str_url_name

    def display_organity_name(self):
        return self.organity.name if self.organity_name is None else self.organity_name

    def display_url_name(self):
        return self.url.name if self.genre_name is None else self.genre_name


class RelationOrganityUrlType(RelationType):
    pass


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


class RelationWorkWorkType(RelationType):
    pass


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


class RelationWorkCharacterType(RelationType):
    pass


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


class RelationWorkGenreType(RelationType):
    pass


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


class RelationWorkUrlType(RelationType):
    pass


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


class RelationCharacterCharacterType(RelationType):
    pass


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


class RelationCharacterGenreType(RelationType):
    pass


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


class RelationCharacterUrlType(RelationType):
    pass


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


class RelationGenreGenreType(RelationType):
    pass


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


class RelationGenreUrlType(RelationType):
    pass


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


class RelationUrlUrlType(RelationType):
    pass

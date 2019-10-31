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
class Relation(models.Model):
    entity_a = None
    entity_b = None
    relation_type = None
    entity_a_name = models.CharField(max_length=200, help_text='If first entity was credited differently', blank=True, null=True)
    entity_b_name = models.CharField(max_length=200, help_text='If second entity was credited differently', blank=True, null=True)
    relation_name = models.CharField(max_length=200, help_text='A name for the relation', blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True, help_text='When did the relation start?')
    end_date = models.DateField(blank=True, null=True, help_text='When did the relation end?')
    highlighted_relation = models.BooleanField(null=True, blank=True)
    inverted_relation = models.BooleanField(default=False)

    def __str__(self):
        str_entity_a_name = self.display_entity_a_name()
        str_entity_b_name = self.display_entity_b_name()
        str_relation = self.display_relation_name()
        return str_entity_a_name + ' <' + str_relation + '> ' + str_entity_b_name if not self.inverted_relation else str_entity_b_name + ' <' + str_relation + '> ' + str_entity_a_name

    def display_entity_a_name(self):
        return str(self.entity_a) if self.entity_a_name is None else self.entity_a_name

    def display_entity_b_name(self):
        return str(self.entity_b) if self.entity_b_name is None else self.entity_b_name

    def display_relation_name(self):
        if self.relation_name is not None:
            return self.relation_name
        if self.relation_type is not None:
            return self.relation_type.name if not self.inverted_relation else self.relation_type.inverted_name
        return "not set"

    class Meta:
        abstract = True


class RelationType(models.Model):
    name = models.CharField(max_length=200, help_text='A name for the x - y relation type', default='relation type')
    inverted_name = models.CharField(max_length=200, help_text='A name for the y - x relation type (inverted)', default='inverted relation type')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class RelationShowShow(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT, related_name='%(app_label)s_%(class)s_show_a')
    entity_b = models.ForeignKey('EntityShow', on_delete=models.PROTECT, related_name='%(app_label)s_%(class)s_show_b')
    relation_type = models.ForeignKey('RelationShowShowType', on_delete=models.PROTECT, blank=True, null=True)


class RelationShowShowType(RelationType):
    pass


class RelationShowProduction(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationShowProductionType', on_delete=models.PROTECT, blank=True, null=True)


class RelationShowProductionType(RelationType):
    pass


class RelationShowOrganity(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    relation_type = models.ForeignKey('RelationShowOrganityType', on_delete=models.PROTECT, blank=True, null=True)


class RelationShowOrganityType(RelationType):
    pass


class RelationShowWork(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationShowWorkType', on_delete=models.PROTECT, blank=True, null=True)


class RelationShowWorkType(RelationType):
    pass


class RelationShowCharacter(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationShowCharacterType', on_delete=models.PROTECT, blank=True, null=True)


class RelationShowCharacterType(RelationType):
    pass


class RelationShowGenre(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationShowGenreType', on_delete=models.PROTECT, blank=True, null=True)


class RelationShowGenreType(RelationType):
    pass


class RelationShowUrl(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationShowUrlType', on_delete=models.PROTECT, blank=True, null=True)


class RelationShowUrlType(RelationType):
    pass


class RelationProductionProduction(Relation):
    entity_a = models.ForeignKey(EntityProduction, on_delete=models.PROTECT, related_name='%(class)s_production_a')
    entity_b = models.ForeignKey(EntityProduction, on_delete=models.PROTECT, related_name='%(class)s_production_b')
    relation_type = models.ForeignKey('RelationProductionProductionType', on_delete=models.PROTECT, blank=True, null=True)


class RelationProductionProductionType(RelationType):
    pass


class RelationProductionOrganity(Relation):
    entity_a = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    relation_type = models.ForeignKey('RelationProductionOrganityType', on_delete=models.PROTECT, blank=True, null=True)


class RelationProductionOrganityType(RelationType):
    pass


class RelationProductionWork(Relation):
    entity_a = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationProductionWorkType', on_delete=models.PROTECT, blank=True, null=True)


class RelationProductionWorkType(RelationType):
    pass


class RelationProductionCharacter(Relation):
    entity_a = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationProductionCharacterType', on_delete=models.PROTECT, blank=True, null=True)


class RelationProductionCharacterType(RelationType):
    pass


class RelationProductionGenre(Relation):
    entity_a = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationProductionGenreType', on_delete=models.PROTECT, blank=True, null=True)


class RelationProductionGenreType(RelationType):
    pass


class RelationProductionUrl(Relation):
    entity_a = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationProductionUrlType', on_delete=models.PROTECT, blank=True, null=True)


class RelationProductionUrlType(RelationType):
    pass


class RelationOrganityOrganity(Relation):
    entity_a = models.ForeignKey(EntityOrganity, on_delete=models.PROTECT, related_name='%(class)s_organity_a')
    entity_b = models.ForeignKey(EntityOrganity, on_delete=models.PROTECT, related_name='%(class)s_organity_b')
    relation_type = models.ForeignKey('RelationOrganityOrganityType', on_delete=models.PROTECT, blank=True, null=True)


class RelationOrganityOrganityType(RelationType):
    pass


class RelationOrganityWork(Relation):
    entity_a = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    entity_b = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationOrganityWorkType', on_delete=models.PROTECT, blank=True, null=True)


class RelationOrganityWorkType(RelationType):
    pass


class RelationOrganityCharacter(Relation):
    entity_a = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    entity_b = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationOrganityCharacterType', on_delete=models.PROTECT, blank=True, null=True)


class RelationOrganityCharacterType(RelationType):
    pass


class RelationOrganityGenre(Relation):
    entity_a = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    entity_b = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationOrganityGenreType', on_delete=models.PROTECT, blank=True, null=True)


class RelationOrganityGenreType(RelationType):
    pass


class RelationOrganityUrl(Relation):
    entity_a = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, default='provide a value here')
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationOrganityUrlType', on_delete=models.PROTECT, blank=True, null=True)


class RelationOrganityUrlType(RelationType):
    pass


class RelationWorkWork(Relation):
    entity_a = models.ForeignKey(EntityWork, on_delete=models.PROTECT, related_name='%(class)s_work_a')
    entity_b = models.ForeignKey(EntityWork, on_delete=models.PROTECT, related_name='%(class)s_work_b')
    relation_type = models.ForeignKey('RelationWorkWorkType', on_delete=models.PROTECT, blank=True, null=True)


class RelationWorkWorkType(RelationType):
    pass


class RelationWorkCharacter(Relation):
    entity_a = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationWorkCharacterType', on_delete=models.PROTECT, blank=True, null=True)


class RelationWorkCharacterType(RelationType):
    pass


class RelationWorkGenre(Relation):
    entity_a = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationWorkGenreType', on_delete=models.PROTECT, blank=True, null=True)


class RelationWorkGenreType(RelationType):
    pass


class RelationWorkUrl(Relation):
    entity_a = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationWorkUrlType', on_delete=models.PROTECT, blank=True, null=True)


class RelationWorkUrlType(RelationType):
    pass


class RelationCharacterCharacter(Relation):
    entity_a = models.ForeignKey(EntityCharacter, on_delete=models.PROTECT, related_name='%(class)s_character_a')
    entity_b = models.ForeignKey(EntityCharacter, on_delete=models.PROTECT, related_name='%(class)s_character_b')
    relation_type = models.ForeignKey('RelationCharacterCharacterType', on_delete=models.PROTECT, blank=True, null=True)


class RelationCharacterCharacterType(RelationType):
    pass


class RelationCharacterGenre(Relation):
    entity_a = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationCharacterGenreType', on_delete=models.PROTECT, blank=True, null=True)


class RelationCharacterGenreType(RelationType):
    pass


class RelationCharacterUrl(Relation):
    entity_a = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationCharacterUrlType', on_delete=models.PROTECT, blank=True, null=True)


class RelationCharacterUrlType(RelationType):
    pass


class RelationGenreGenre(Relation):
    entity_a = models.ForeignKey(EntityGenre, on_delete=models.PROTECT, related_name='%(class)s_genre_a')
    entity_b = models.ForeignKey(EntityGenre, on_delete=models.PROTECT, related_name='%(class)s_genre_b')
    relation_type = models.ForeignKey('RelationGenreGenreType', on_delete=models.PROTECT, blank=True, null=True)


class RelationGenreGenreType(RelationType):
    pass


class RelationGenreUrl(Relation):
    entity_a = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ForeignKey('RelationGenreUrlType', on_delete=models.PROTECT, blank=True, null=True)


class RelationGenreUrlType(RelationType):
    pass


class RelationUrlUrl(Relation):
    entity_a = models.ForeignKey(EntityUrl, on_delete=models.PROTECT, related_name='%(class)s_url_a')
    entity_b = models.ForeignKey(EntityUrl, on_delete=models.PROTECT, related_name='%(class)s_url_b')
    relation_type = models.ForeignKey('RelationUrlUrlType', on_delete=models.PROTECT, blank=True, null=True)


class RelationUrlUrlType(RelationType):
    pass

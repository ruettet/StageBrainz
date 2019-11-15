from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from partial_date import PartialDateField


# Create your models here.
class Entity(models.Model):
    entity_type = None
    entity_type_str = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, default="")
    sort_name = models.CharField(max_length=200, default="")
    disambiguation = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['sort_name']


class EntityType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class EntityAlias(models.Model):
    super_entity = None
    alias_type = None
    locale = models.ForeignKey('Locale', on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class EntityAliasType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class EntityShow(Entity):
    when_date = PartialDateField(blank=True, null=True)
    when_time = models.TimeField(blank=True, null=True)
    entity_type = models.ManyToManyField('EntityShowType', blank=True)

    def display_show_name_with_date_and_time(self):
        output = self.name + ", " + self.display_show_when()
        return output

    def display_show_when(self):
        date_iso = str(self.when_date)
        return date_iso + ", " + self.when_time.isoformat() if self.when_time is not None else date_iso

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this show"""
        return reverse('shows-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-when_date', '-when_time']


class EntityShowType(EntityType):
    pass


class EntityProduction(Entity):
    """"Model representing stage productions"""
    season = models.ForeignKey('Season', on_delete=models.PROTECT, blank=True, null=True)
    start_date = PartialDateField(blank=True, null=True, default=None)
    end_date = PartialDateField(blank=True, null=True, default=None)
    entity_type = models.ManyToManyField('EntityProductionType', blank=True)

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this production"""
        return reverse('productions-detail', args=[str(self.id)])


class EntityProductionType(EntityType):
    pass


class Season(models.Model):
    """"Model representing a traditional season"""
    name = models.CharField(max_length=200)
    start_date = PartialDateField(blank=True, null=True, default=None)
    end_date = PartialDateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Locale(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EntityOrganity(Entity):
    entity_type = models.ManyToManyField('EntityOrganityType', blank=True)
    start_date = PartialDateField(blank=True, null=True, default=None)
    end_date = PartialDateField(blank=True, null=True, default=None)

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this production"""
        return reverse('organities-detail', args=[str(self.id)])


class EntityOrganityType(EntityType):
    pass


class EntityOrganityAlias(EntityAlias):
    super_entity = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT)
    alias_type = models.ForeignKey('EntityOrganityAliasType', on_delete=models.PROTECT)

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this production"""
        return reverse('organityaliases-detail', args=[str(self.id)])


class EntityOrganityAliasType(EntityAliasType):
    pass


class EntityWork(Entity):
    entity_type = models.ManyToManyField('EntityWorkType', blank=True)
    start_date = models.CharField(max_length=10, default="")

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this venue"""
        return reverse('works-detail', args=[str(self.id)])


class EntityWorkType(EntityType):
    pass


class EntityWorkAlias(EntityAlias):
    super_entity = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    alias_type = models.ForeignKey('EntityWorkAliasType', on_delete=models.PROTECT)


class EntityWorkAliasType(models.Model):
    pass


class EntityCharacter(Entity):
    entity_type = models.ManyToManyField('EntityCharacterType', blank=True)

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this character"""
        return reverse('characters-detail', args=[str(self.id)])


class EntityCharacterType(EntityType):
    pass


class EntityCharacterAlias(models.Model):
    super_entity = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    alias_type = models.ForeignKey('EntityCharacterAliasType', on_delete=models.PROTECT)


class EntityCharacterAliasType(models.Model):
    pass


class EntityGenre(Entity):
    entity_type = models.ManyToManyField('EntityGenreType', blank=True)

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this genre"""
        return reverse('genres-detail', args=[str(self.id)])


class EntityGenreType(EntityType):
    pass


class EntityGenreAlias(EntityAlias):
    super_entity = models.ForeignKey(EntityGenre, on_delete=models.PROTECT)
    alias_type = models.ForeignKey('EntityGenreAliasType', on_delete=models.PROTECT)


class EntityGenreAliasType(EntityAliasType):
    pass


class EntityUrl(Entity):
    name = models.URLField(max_length=200)
    sort_name = None
    entity_type = models.ManyToManyField('EntityUrlType', blank=True)

    def get_absolute_url(self):
        """"Returns the url to access a detail record for this show"""
        return reverse('url-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']


class EntityUrlType(EntityType):
    pass


# Relations
class Relation(models.Model):
    entity_a = None
    entity_b = None
    relation_type = None
    entity_a_credited_as = models.CharField(max_length=200, blank=True, null=True)
    entity_b_credited_as = models.CharField(max_length=200, blank=True, null=True)
    relation_name = models.CharField(max_length=200, blank=True, null=True)
    start_date = PartialDateField(blank=True, null=True, default=None)
    end_date = PartialDateField(blank=True, null=True, default=None)
    highlighted_relation = models.BooleanField(null=True, blank=True)
    inverted_relation = models.BooleanField(default=False)
    context_of_production = models.ForeignKey('EntityProduction', on_delete=models.PROTECT, related_name='%(class)s_context_production', null=True, blank=True)
    context_of_production_str = models.CharField(max_length=200, null=True, blank=True)
    context_of_show = models.ForeignKey('EntityShow', on_delete=models.PROTECT, related_name='%(class)s_context_show', null=True, blank=True)
    context_of_show_str = models.CharField(max_length=200, null=True, blank=True)
    context_of_work = models.ForeignKey('EntityWork', on_delete=models.PROTECT, related_name='%(class)s_context_work', null=True, blank=True)
    context_of_work_str = models.CharField(max_length=200, null=True, blank=True)
    context_of_character = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT, related_name='%(class)s_context_character', null=True, blank=True)
    context_of_character_str = models.CharField(max_length=200, null=True, blank=True)
    context_of_organity = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, related_name='%(class)s_context_organity', null=True, blank=True)
    context_of_organity_str = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        str_entity_a_name = self.display_entity_a_name()
        str_entity_b_name = self.display_entity_b_name()
        str_relation = self.display_relation_name()
        return str_entity_a_name + ' <' + str_relation + '> ' + str_entity_b_name if not self.inverted_relation else str_entity_b_name + ' <' + str_relation + '> ' + str_entity_a_name

    def display_entity_a_name(self):
        return str(self.entity_a) if self.entity_a_credited_as is None else self.entity_a_credited_as

    def display_entity_b_name(self):
        return str(self.entity_b) if self.entity_b_credited_as is None else self.entity_b_credited_as

    def display_relation_name(self):
        if self.relation_name is not None:
            return self.relation_name
        if self.relation_type.count() > 0:
            if self.inverted_relation:
                return ", ".join([r.inverted_name for r in self.relation_type.all()])
            else:
                return ", ".join([r.name for r in self.relation_type.all()])
        return "not set"

    def display_context_of_character(self):
        return self.context_of_character.name if self.context_of_character_str is None else self.context_of_character_str

    class Meta:
        abstract = True


class RelationType(models.Model):
    name = models.CharField(max_length=200)
    inverted_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class RelationShowShow(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT, related_name='showa')
    entity_b = models.ForeignKey('EntityShow', on_delete=models.PROTECT, related_name='showb')
    relation_type = models.ManyToManyField('RelationShowShowType')


class RelationShowShowType(RelationType):
    pass


class RelationShowProduction(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    relation_type = models.ManyToManyField('RelationShowProductionType')

    class Meta:
        ordering = ['entity_a']


class RelationShowProductionType(RelationType):
    pass


class RelationShowOrganity(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT)
    relation_type = models.ManyToManyField('RelationShowOrganityType')


class RelationShowOrganityType(RelationType):
    pass


class RelationShowWork(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    relation_type = models.ManyToManyField('RelationShowWorkType')


class RelationShowWorkType(RelationType):
    pass


class RelationShowCharacter(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    relation_type = models.ManyToManyField('RelationShowCharacterType')


class RelationShowCharacterType(RelationType):
    pass


class RelationShowGenre(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    relation_type = models.ManyToManyField('RelationShowGenreType')


class RelationShowGenreType(RelationType):
    pass


class RelationShowUrl(Relation):
    entity_a = models.ForeignKey('EntityShow', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ManyToManyField('RelationShowUrlType')


class RelationShowUrlType(RelationType):
    pass


class RelationProductionProduction(Relation):
    entity_a = models.ForeignKey(EntityProduction, on_delete=models.PROTECT, related_name='productiona')
    entity_b = models.ForeignKey(EntityProduction, on_delete=models.PROTECT, related_name='productionb')
    relation_type = models.ManyToManyField('RelationProductionProductionType')


class RelationProductionProductionType(RelationType):
    pass


class RelationProductionOrganity(Relation):
    entity_a = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT, blank=True, null=True)
    relation_type = models.ManyToManyField('RelationProductionOrganityType')

    class Meta:
        ordering = ['-highlighted_relation', 'entity_b']


class RelationProductionOrganityType(RelationType):
    pass


class RelationProductionWork(Relation):
    entity_a = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityWork', on_delete=models.PROTECT, blank=True, null=True)
    relation_type = models.ManyToManyField('RelationProductionWorkType')


class RelationProductionWorkType(RelationType):
    pass


class RelationProductionCharacter(Relation):
    entity_a = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT, blank=True, null=True)
    relation_type = models.ManyToManyField('RelationProductionCharacterType')


class RelationProductionCharacterType(RelationType):
    pass


class RelationProductionGenre(Relation):
    entity_a = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityGenre', on_delete=models.PROTECT, blank=True, null=True)
    relation_type = models.ManyToManyField('RelationProductionGenreType')


class RelationProductionGenreType(RelationType):
    pass


class RelationProductionUrl(Relation):
    entity_a = models.ForeignKey('EntityProduction', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ManyToManyField('RelationProductionUrlType')


class RelationProductionUrlType(RelationType):
    pass


class RelationOrganityOrganity(Relation):
    entity_a = models.ForeignKey(EntityOrganity, on_delete=models.PROTECT, related_name='organitya')
    entity_b = models.ForeignKey(EntityOrganity, on_delete=models.PROTECT, related_name='organityb')
    relation_type = models.ManyToManyField('RelationOrganityOrganityType')


class RelationOrganityOrganityType(RelationType):
    pass


class RelationOrganityWork(Relation):
    entity_a = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityWork', on_delete=models.PROTECT, blank=True, null=True)
    relation_type = models.ManyToManyField('RelationOrganityWorkType')


class RelationOrganityWorkType(RelationType):
    pass


class RelationOrganityCharacter(Relation):
    entity_a = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT, blank=True, null=True)
    relation_type = models.ManyToManyField('RelationOrganityCharacterType')


class RelationOrganityCharacterType(RelationType):
    pass


class RelationOrganityGenre(Relation):
    entity_a = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityGenre', on_delete=models.PROTECT, blank=True, null=True)
    relation_type = models.ManyToManyField('RelationOrganityGenreType')


class RelationOrganityGenreType(RelationType):
    pass


class RelationOrganityUrl(Relation):
    entity_a = models.ForeignKey('EntityOrganity', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ManyToManyField('RelationOrganityUrlType')


class RelationOrganityUrlType(RelationType):
    pass


class RelationWorkWork(Relation):
    entity_a = models.ForeignKey(EntityWork, on_delete=models.PROTECT, related_name='worka')
    entity_b = models.ForeignKey(EntityWork, on_delete=models.PROTECT, related_name='workb')
    relation_type = models.ManyToManyField('RelationWorkWorkType')


class RelationWorkWorkType(RelationType):
    pass


class RelationWorkCharacter(Relation):
    entity_a = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT, blank=True, null=True)
    relation_type = models.ManyToManyField('RelationWorkCharacterType')


class RelationWorkCharacterType(RelationType):
    pass


class RelationWorkGenre(Relation):
    entity_a = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityGenre', on_delete=models.PROTECT, blank=True, null=True)
    relation_type = models.ManyToManyField('RelationWorkGenreType')


class RelationWorkGenreType(RelationType):
    pass


class RelationWorkUrl(Relation):
    entity_a = models.ForeignKey('EntityWork', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ManyToManyField('RelationWorkUrlType')


class RelationWorkUrlType(RelationType):
    pass


class RelationCharacterCharacter(Relation):
    entity_a = models.ForeignKey(EntityCharacter, on_delete=models.PROTECT, related_name='charactera')
    entity_b = models.ForeignKey(EntityCharacter, on_delete=models.PROTECT, related_name='characterb')
    relation_type = models.ManyToManyField('RelationCharacterCharacterType')


class RelationCharacterCharacterType(RelationType):
    pass


class RelationCharacterGenre(Relation):
    entity_a = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityGenre', on_delete=models.PROTECT, blank=True, null=True)
    relation_type = models.ManyToManyField('RelationCharacterGenreType')


class RelationCharacterGenreType(RelationType):
    pass


class RelationCharacterUrl(Relation):
    entity_a = models.ForeignKey('EntityCharacter', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ManyToManyField('RelationCharacterUrlType')


class RelationCharacterUrlType(RelationType):
    pass


class RelationGenreGenre(Relation):
    entity_a = models.ForeignKey(EntityGenre, on_delete=models.PROTECT, related_name='genrea')
    entity_b = models.ForeignKey(EntityGenre, on_delete=models.PROTECT, related_name='genreb')
    relation_type = models.ManyToManyField('RelationGenreGenreType')


class RelationGenreGenreType(RelationType):
    pass


class RelationGenreUrl(Relation):
    entity_a = models.ForeignKey('EntityGenre', on_delete=models.PROTECT)
    entity_b = models.ForeignKey('EntityUrl', on_delete=models.PROTECT)
    relation_type = models.ManyToManyField('RelationGenreUrlType')


class RelationGenreUrlType(RelationType):
    pass


class RelationUrlUrl(Relation):
    entity_a = models.ForeignKey(EntityUrl, on_delete=models.PROTECT, related_name='urla')
    entity_b = models.ForeignKey(EntityUrl, on_delete=models.PROTECT, related_name='urlb')
    relation_type = models.ManyToManyField('RelationUrlUrlType')


class RelationUrlUrlType(RelationType):
    pass

from django.contrib import admin
from catalog.models import EntityShow, EntityShowType, \
    EntityVenue, EntityVenueType, EntityVenueAlias, EntityVenueAliasType, \
    EntityProduction, EntityProductionType, \
    EntitySeason, \
    EntityPerson, EntityPersonType, EntityPersonAlias, EntityPersonAliasType, \
    EntityOrganisation, EntityOrganisationType, EntityOrganisationAlias, EntityOrganisationAliasType, \
    EntityWork, EntityWorkType, EntityWorkAlias, EntityWorkAliasType, \
    EntityCharacter, EntityCharacterType, EntityCharacterAlias, EntityCharacterAliasType, \
    EntityGenre, EntityGenreType, EntityGenreAlias, EntityGenreAliasType, \
    EntityUrl, EntityUrlType, \
    RelationShowShow, RelationShowShowType, \
    RelationShowVenue, RelationShowVenueType,\
    RelationShowProduction, RelationShowProductionType, \
    RelationShowPerson, RelationShowPersonType, \
    RelationShowOrganisation, RelationShowOrganisationType, \
    RelationShowWork, RelationShowWorkType, \
    RelationShowCharacter, RelationShowCharacterType, \
    RelationShowGenre, RelationShowGenreType, \
    RelationShowUrl, RelationShowUrlType, \
    RelationVenueVenue, RelationVenueVenueType, \
    RelationVenueProduction, RelationVenueProductionType, \
    RelationVenuePerson, RelationVenuePersonType, \
    RelationVenueOrganisation, RelationVenueOrganisationType, \
    RelationVenueWork, RelationVenueWorkType, \
    RelationVenueCharacter, RelationVenueCharacterType, \
    RelationVenueGenre, RelationVenueGenreType, \
    RelationVenueUrl, RelationVenueUrlType, \
    RelationProductionProduction, RelationProductionProductionType, \
    RelationProductionPerson, RelationProductionPersonType, \
    RelationProductionOrganisation, RelationProductionOrganisationType, \
    RelationProductionWork, RelationProductionWorkType, \
    RelationProductionCharacter, RelationProductionCharacterType, \
    RelationProductionGenre, RelationProductionGenreType, \
    RelationProductionUrl, RelationProductionUrlType, \
    RelationPersonPerson, RelationPersonPersonType, \
    RelationPersonOrganisation, RelationPersonOrganisationType, \
    RelationPersonWork, RelationPersonWorkType, \
    RelationPersonCharacter, RelationPersonCharacterType, \
    RelationPersonGenre, RelationPersonGenreType, \
    RelationPersonUrl, RelationPersonUrlType, \
    RelationOrganisationOrganisation, RelationOrganisationOrganisationType, \
    RelationOrganisationWork, RelationOrganisationWorkType, \
    RelationOrganisationCharacter, RelationOrganisationCharacterType, \
    RelationOrganisationGenre, RelationOrganisationGenreType, \
    RelationOrganisationUrl, RelationOrganisationUrlType, \
    RelationWorkWork, RelationWorkWorkType, \
    RelationWorkCharacter, RelationWorkCharacterType, \
    RelationWorkGenre, RelationWorkGenreType, \
    RelationWorkUrl, RelationWorkUrlType, \
    RelationCharacterCharacter, RelationCharacterCharacterType, \
    RelationCharacterGenre, RelationCharacterGenreType, \
    RelationCharacterUrl, RelationCharacterUrlType, \
    RelationGenreGenre, RelationGenreGenreType, \
    RelationGenreUrl, RelationGenreUrlType, \
    RelationUrlUrl, RelationUrlUrlType


# Register your models here.
# Define the admin class
# inlines
class RelationShowVenueInline(admin.TabularInline):
    model = RelationShowVenue
    ordering = ('show', )


class VenueAliasInline(admin.TabularInline):
    model = EntityVenueAlias


# relations
class RelationShowVenueAdmin(admin.ModelAdmin):
    list_display = ('display_show_name', 'display_venue_name', 'display_show_when')


class RelationShowVenueTypeAdmin(admin.ModelAdmin):
    pass


class RelationShowShowAdmin(admin.ModelAdmin):
    pass


class RelationShowShowTypeAdmin(admin.ModelAdmin):
    pass


class RelationShowProductionAdmin(admin.ModelAdmin):
    pass


class RelationShowProductionTypeAdmin(admin.ModelAdmin):
    pass


class RelationShowPersonAdmin(admin.ModelAdmin):
    pass


class RelationShowPersonTypeAdmin(admin.ModelAdmin):
    pass


class RelationShowOrganisationAdmin(admin.ModelAdmin):
    pass


class RelationShowOrganisationTypeAdmin(admin.ModelAdmin):
    pass


class RelationShowWorkAdmin(admin.ModelAdmin):
    pass


class RelationShowWorkTypeAdmin(admin.ModelAdmin):
    pass


class RelationShowCharacterAdmin(admin.ModelAdmin):
    pass


class RelationShowCharacterTypeAdmin(admin.ModelAdmin):
    pass


class RelationShowGenreAdmin(admin.ModelAdmin):
    pass


class RelationShowGenreTypeAdmin(admin.ModelAdmin):
    pass


class RelationShowUrlAdmin(admin.ModelAdmin):
    pass


class RelationShowUrlTypeAdmin(admin.ModelAdmin):
    pass


class RelationVenueVenueAdmin(admin.ModelAdmin):
    pass


class RelationVenueVenueTypeAdmin(admin.ModelAdmin):
    pass


class RelationVenueProductionAdmin(admin.ModelAdmin):
    pass


class RelationVenueProductionTypeAdmin(admin.ModelAdmin):
    pass


class RelationVenuePersonAdmin(admin.ModelAdmin):
    pass


class RelationVenuePersonTypeAdmin(admin.ModelAdmin):
    pass


class RelationVenueOrganisationAdmin(admin.ModelAdmin):
    pass


class RelationVenueOrganisationTypeAdmin(admin.ModelAdmin):
    pass


class RelationVenueWorkAdmin(admin.ModelAdmin):
    pass


class RelationVenueWorkTypeAdmin(admin.ModelAdmin):
    pass


class RelationVenueCharacterAdmin(admin.ModelAdmin):
    pass


class RelationVenueCharacterTypeAdmin(admin.ModelAdmin):
    pass


class RelationVenueGenreAdmin(admin.ModelAdmin):
    pass


class RelationVenueGenreTypeAdmin(admin.ModelAdmin):
    pass


class RelationVenueUrlAdmin(admin.ModelAdmin):
    pass


class RelationVenueUrlTypeAdmin(admin.ModelAdmin):
    pass


class RelationProductionProductionAdmin(admin.ModelAdmin):
    pass


class RelationProductionProductionTypeAdmin(admin.ModelAdmin):
    pass


class RelationProductionPersonAdmin(admin.ModelAdmin):
    pass


class RelationProductionPersonTypeAdmin(admin.ModelAdmin):
    pass


class RelationProductionOrganisationAdmin(admin.ModelAdmin):
    pass


class RelationProductionOrganisationTypeAdmin(admin.ModelAdmin):
    pass


class RelationProductionWorkAdmin(admin.ModelAdmin):
    pass


class RelationProductionWorkTypeAdmin(admin.ModelAdmin):
    pass


class RelationProductionCharacterAdmin(admin.ModelAdmin):
    pass


class RelationProductionCharacterTypeAdmin(admin.ModelAdmin):
    pass


class RelationProductionGenreAdmin(admin.ModelAdmin):
    pass


class RelationProductionGenreTypeAdmin(admin.ModelAdmin):
    pass


class RelationProductionUrlAdmin(admin.ModelAdmin):
    pass


class RelationProductionUrlTypeAdmin(admin.ModelAdmin):
    pass


class RelationPersonPersonAdmin(admin.ModelAdmin):
    pass


class RelationPersonPersonTypeAdmin(admin.ModelAdmin):
    pass


class RelationPersonOrganisationAdmin(admin.ModelAdmin):
    pass


class RelationPersonOrganisationTypeAdmin(admin.ModelAdmin):
    pass


class RelationPersonWorkAdmin(admin.ModelAdmin):
    pass


class RelationPersonWorkTypeAdmin(admin.ModelAdmin):
    pass


class RelationPersonCharacterAdmin(admin.ModelAdmin):
    pass


class RelationPersonCharacterTypeAdmin(admin.ModelAdmin):
    pass


class RelationPersonGenreAdmin(admin.ModelAdmin):
    pass


class RelationPersonGenreTypeAdmin(admin.ModelAdmin):
    pass


class RelationPersonUrlAdmin(admin.ModelAdmin):
    pass


class RelationPersonUrlTypeAdmin(admin.ModelAdmin):
    pass


class RelationOrganisationOrganisationAdmin(admin.ModelAdmin):
    pass


class RelationOrganisationOrganisationTypeAdmin(admin.ModelAdmin):
    pass


class RelationOrganisationWorkAdmin(admin.ModelAdmin):
    pass


class RelationOrganisationWorkTypeAdmin(admin.ModelAdmin):
    pass


class RelationOrganisationCharacterAdmin(admin.ModelAdmin):
    pass


class RelationOrganisationCharacterTypeAdmin(admin.ModelAdmin):
    pass


class RelationOrganisationGenreAdmin(admin.ModelAdmin):
    pass


class RelationOrganisationGenreTypeAdmin(admin.ModelAdmin):
    pass


class RelationOrganisationUrlAdmin(admin.ModelAdmin):
    pass


class RelationOrganisationUrlTypeAdmin(admin.ModelAdmin):
    pass


class RelationWorkWorkAdmin(admin.ModelAdmin):
    pass


class RelationWorkWorkTypeAdmin(admin.ModelAdmin):
    pass


class RelationWorkCharacterAdmin(admin.ModelAdmin):
    pass


class RelationWorkCharacterTypeAdmin(admin.ModelAdmin):
    pass


class RelationWorkGenreAdmin(admin.ModelAdmin):
    pass


class RelationWorkGenreTypeAdmin(admin.ModelAdmin):
    pass


class RelationWorkUrlAdmin(admin.ModelAdmin):
    pass


class RelationWorkUrlTypeAdmin(admin.ModelAdmin):
    pass


class RelationCharacterCharacterAdmin(admin.ModelAdmin):
    pass


class RelationCharacterCharacterTypeAdmin(admin.ModelAdmin):
    pass


class RelationCharacterGenreAdmin(admin.ModelAdmin):
    pass


class RelationCharacterGenreTypeAdmin(admin.ModelAdmin):
    pass


class RelationCharacterUrlAdmin(admin.ModelAdmin):
    pass


class RelationCharacterUrlTypeAdmin(admin.ModelAdmin):
    pass


class RelationGenreGenreAdmin(admin.ModelAdmin):
    pass


class RelationGenreGenreTypeAdmin(admin.ModelAdmin):
    pass


class RelationGenreUrlAdmin(admin.ModelAdmin):
    pass


class RelationGenreUrlTypeAdmin(admin.ModelAdmin):
    pass


class RelationUrlUrlAdmin(admin.ModelAdmin):
    pass


class RelationUrlUrlTypeAdmin(admin.ModelAdmin):
    pass


#entities
class EntityShowAdmin(admin.ModelAdmin):
    list_display = ('display_show_name_with_date_and_time', 'when_date', 'when_time')
    list_filter = ('when_date',)


class EntityShowTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EntityVenueAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [VenueAliasInline]


class EntityVenueTypeAdmin(admin.ModelAdmin):
    pass


class EntityVenueAliasAdmin(admin.ModelAdmin):
    pass


class EntityVenueAliasTypeAdmin(admin.ModelAdmin):
    pass


class EntityProductionAdmin(admin.ModelAdmin):
    pass


class EntityProductionTypeAdmin(admin.ModelAdmin):
    pass


class EntitySeasonAdmin(admin.ModelAdmin):
    pass


class EntityPersonAdmin(admin.ModelAdmin):
    list_filter = ('person_type',)


class EntityPersonTypeAdmin(admin.ModelAdmin):
    pass


class EntityPersonAliasAdmin(admin.ModelAdmin):
    pass


class EntityPersonAliasTypeAdmin(admin.ModelAdmin):
    pass


class EntityOrganisationAdmin(admin.ModelAdmin):
    list_filter = ('organisation_type',)


class EntityOrganisationTypeAdmin(admin.ModelAdmin):
    pass


class EntityOrganisationAliasAdmin(admin.ModelAdmin):
    pass


class EntityOrganisationAliasTypeAdmin(admin.ModelAdmin):
    pass


class EntityWorkAdmin(admin.ModelAdmin):
    list_filter = ('work_type',)


class EntityWorkTypeAdmin(admin.ModelAdmin):
    pass


class EntityWorkAliasAdmin(admin.ModelAdmin):
    pass


class EntityWorkAliasTypeAdmin(admin.ModelAdmin):
    pass


class EntityCharacterAdmin(admin.ModelAdmin):
    list_filter = ('character_type',)


class EntityCharacterTypeAdmin(admin.ModelAdmin):
    pass


class EntityCharacterAliasAdmin(admin.ModelAdmin):
    pass


class EntityCharacterAliasTypeAdmin(admin.ModelAdmin):
    pass


class EntityGenreAdmin(admin.ModelAdmin):
    list_filter = ('genre_type',)


class EntityGenreTypeAdmin(admin.ModelAdmin):
    pass


class EntityGenreAliasAdmin(admin.ModelAdmin):
    pass


class EntityGenreAliasTypeAdmin(admin.ModelAdmin):
    pass


class EntityUrlAdmin(admin.ModelAdmin):
    list_filter = ('url_type',)


class EntityUrlTypeAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
# shows
admin.site.register(EntityShow, EntityShowAdmin)
admin.site.register(EntityShowType, EntityShowTypeAdmin)

# venues
admin.site.register(EntityVenue, EntityVenueAdmin)
admin.site.register(EntityVenueType, EntityVenueTypeAdmin)
admin.site.register(EntityVenueAlias, EntityVenueAliasAdmin)
admin.site.register(EntityVenueAliasType, EntityVenueAliasTypeAdmin)

# productions
admin.site.register(EntityProduction, EntityProductionAdmin)
admin.site.register(EntityProductionType, EntityProductionTypeAdmin)

# seasons
admin.site.register(EntitySeason, EntitySeasonAdmin)

# people
admin.site.register(EntityPerson, EntityPersonAdmin)
admin.site.register(EntityPersonType, EntityPersonTypeAdmin)
admin.site.register(EntityPersonAlias, EntityPersonAliasAdmin)
admin.site.register(EntityPersonAliasType, EntityPersonAliasTypeAdmin)

# organisations
admin.site.register(EntityOrganisation, EntityOrganisationAdmin)
admin.site.register(EntityOrganisationType, EntityOrganisationTypeAdmin)
admin.site.register(EntityOrganisationAlias, EntityOrganisationAliasAdmin)
admin.site.register(EntityOrganisationAliasType, EntityOrganisationAliasTypeAdmin)

# works
admin.site.register(EntityWork, EntityWorkAdmin)
admin.site.register(EntityWorkType, EntityWorkTypeAdmin)
admin.site.register(EntityWorkAlias, EntityWorkAliasAdmin)
admin.site.register(EntityWorkAliasType, EntityWorkAliasTypeAdmin)

# characters
admin.site.register(EntityCharacter, EntityCharacterAdmin)
admin.site.register(EntityCharacterType, EntityCharacterTypeAdmin)
admin.site.register(EntityCharacterAlias, EntityCharacterAliasAdmin)
admin.site.register(EntityCharacterAliasType, EntityCharacterAliasTypeAdmin)

# genres
admin.site.register(EntityGenre, EntityGenreAdmin)
admin.site.register(EntityGenreType, EntityGenreTypeAdmin)
admin.site.register(EntityGenreAlias, EntityGenreAliasAdmin)
admin.site.register(EntityGenreAliasType, EntityGenreAliasTypeAdmin)

# urls
admin.site.register(EntityUrl, EntityUrlAdmin)
admin.site.register(EntityUrlType, EntityUrlTypeAdmin)

# relations
admin.site.register(RelationShowShow, RelationShowShowAdmin)
admin.site.register(RelationShowShowType, RelationShowShowTypeAdmin)
admin.site.register(RelationShowVenue, RelationShowVenueAdmin)
admin.site.register(RelationShowVenueType, RelationShowVenueTypeAdmin)
admin.site.register(RelationShowProduction, RelationShowProductionAdmin)
admin.site.register(RelationShowProductionType, RelationShowProductionTypeAdmin)
admin.site.register(RelationShowPerson, RelationShowPersonAdmin)
admin.site.register(RelationShowPersonType, RelationShowPersonTypeAdmin)
admin.site.register(RelationShowOrganisation, RelationShowOrganisationAdmin)
admin.site.register(RelationShowOrganisationType, RelationShowOrganisationTypeAdmin)
admin.site.register(RelationShowWork, RelationShowWorkAdmin)
admin.site.register(RelationShowWorkType, RelationShowWorkTypeAdmin)
admin.site.register(RelationShowCharacter, RelationShowCharacterAdmin)
admin.site.register(RelationShowCharacterType, RelationShowCharacterTypeAdmin)
admin.site.register(RelationShowGenre, RelationShowGenreAdmin)
admin.site.register(RelationShowGenreType, RelationShowGenreTypeAdmin)
admin.site.register(RelationShowUrl, RelationShowUrlAdmin)
admin.site.register(RelationShowUrlType, RelationShowUrlTypeAdmin)
admin.site.register(RelationVenueVenue, RelationVenueVenueAdmin)
admin.site.register(RelationVenueVenueType, RelationVenueVenueTypeAdmin)
admin.site.register(RelationVenueProduction, RelationVenueProductionAdmin)
admin.site.register(RelationVenueProductionType, RelationVenueProductionTypeAdmin)
admin.site.register(RelationVenuePerson, RelationVenuePersonAdmin)
admin.site.register(RelationVenuePersonType, RelationVenuePersonTypeAdmin)
admin.site.register(RelationVenueOrganisation, RelationVenueOrganisationAdmin)
admin.site.register(RelationVenueOrganisationType, RelationVenueOrganisationTypeAdmin)
admin.site.register(RelationVenueWork, RelationVenueWorkAdmin)
admin.site.register(RelationVenueWorkType, RelationVenueWorkTypeAdmin)
admin.site.register(RelationVenueCharacter, RelationVenueCharacterAdmin)
admin.site.register(RelationVenueCharacterType, RelationVenueCharacterTypeAdmin)
admin.site.register(RelationVenueGenre, RelationVenueGenreAdmin)
admin.site.register(RelationVenueGenreType, RelationVenueGenreTypeAdmin)
admin.site.register(RelationVenueUrl, RelationVenueUrlAdmin)
admin.site.register(RelationVenueUrlType, RelationVenueUrlTypeAdmin)
admin.site.register(RelationProductionProduction, RelationProductionProductionAdmin)
admin.site.register(RelationProductionProductionType, RelationProductionProductionTypeAdmin)
admin.site.register(RelationProductionPerson, RelationProductionPersonAdmin)
admin.site.register(RelationProductionPersonType, RelationProductionPersonTypeAdmin)
admin.site.register(RelationProductionOrganisation, RelationProductionOrganisationAdmin)
admin.site.register(RelationProductionOrganisationType, RelationProductionOrganisationTypeAdmin)
admin.site.register(RelationProductionWork, RelationProductionWorkAdmin)
admin.site.register(RelationProductionWorkType, RelationProductionWorkTypeAdmin)
admin.site.register(RelationProductionCharacter, RelationProductionCharacterAdmin)
admin.site.register(RelationProductionCharacterType, RelationProductionCharacterTypeAdmin)
admin.site.register(RelationProductionGenre, RelationProductionGenreAdmin)
admin.site.register(RelationProductionGenreType, RelationProductionGenreTypeAdmin)
admin.site.register(RelationProductionUrl, RelationProductionUrlAdmin)
admin.site.register(RelationProductionUrlType, RelationProductionUrlTypeAdmin)
admin.site.register(RelationPersonPerson, RelationPersonPersonAdmin)
admin.site.register(RelationPersonPersonType, RelationPersonPersonTypeAdmin)
admin.site.register(RelationPersonOrganisation, RelationPersonOrganisationAdmin)
admin.site.register(RelationPersonOrganisationType, RelationPersonOrganisationTypeAdmin)
admin.site.register(RelationPersonWork, RelationPersonWorkAdmin)
admin.site.register(RelationPersonWorkType, RelationPersonWorkTypeAdmin)
admin.site.register(RelationPersonCharacter, RelationPersonCharacterAdmin)
admin.site.register(RelationPersonCharacterType, RelationPersonCharacterTypeAdmin)
admin.site.register(RelationPersonGenre, RelationPersonGenreAdmin)
admin.site.register(RelationPersonGenreType, RelationPersonGenreTypeAdmin)
admin.site.register(RelationPersonUrl, RelationPersonUrlAdmin)
admin.site.register(RelationPersonUrlType, RelationPersonUrlTypeAdmin)
admin.site.register(RelationOrganisationOrganisation, RelationOrganisationOrganisationAdmin)
admin.site.register(RelationOrganisationOrganisationType, RelationOrganisationOrganisationTypeAdmin)
admin.site.register(RelationOrganisationWork, RelationOrganisationWorkAdmin)
admin.site.register(RelationOrganisationWorkType, RelationOrganisationWorkTypeAdmin)
admin.site.register(RelationOrganisationCharacter, RelationOrganisationCharacterAdmin)
admin.site.register(RelationOrganisationCharacterType, RelationOrganisationCharacterTypeAdmin)
admin.site.register(RelationOrganisationGenre, RelationOrganisationGenreAdmin)
admin.site.register(RelationOrganisationGenreType, RelationOrganisationGenreTypeAdmin)
admin.site.register(RelationOrganisationUrl, RelationOrganisationUrlAdmin)
admin.site.register(RelationOrganisationUrlType, RelationOrganisationUrlTypeAdmin)
admin.site.register(RelationWorkWork, RelationWorkWorkAdmin)
admin.site.register(RelationWorkWorkType, RelationWorkWorkAdmin)
admin.site.register(RelationWorkCharacter, RelationWorkCharacterAdmin)
admin.site.register(RelationWorkCharacterType, RelationWorkCharacterTypeAdmin)
admin.site.register(RelationWorkGenre, RelationWorkGenreAdmin)
admin.site.register(RelationWorkGenreType, RelationWorkGenreTypeAdmin)
admin.site.register(RelationWorkUrl, RelationWorkUrlAdmin)
admin.site.register(RelationWorkUrlType, RelationWorkUrlTypeAdmin)
admin.site.register(RelationCharacterCharacter, RelationCharacterCharacterAdmin)
admin.site.register(RelationCharacterCharacterType, RelationCharacterCharacterTypeAdmin)
admin.site.register(RelationCharacterGenre, RelationCharacterGenreAdmin)
admin.site.register(RelationCharacterGenreType, RelationCharacterGenreTypeAdmin)
admin.site.register(RelationCharacterUrl, RelationCharacterUrlAdmin)
admin.site.register(RelationCharacterUrlType, RelationCharacterUrlTypeAdmin)
admin.site.register(RelationGenreGenre, RelationGenreGenreAdmin)
admin.site.register(RelationGenreGenreType, RelationGenreGenreTypeAdmin)
admin.site.register(RelationGenreUrl, RelationGenreUrlAdmin)
admin.site.register(RelationGenreUrlType, RelationGenreUrlTypeAdmin)
admin.site.register(RelationUrlUrl, RelationUrlUrlAdmin)
admin.site.register(RelationUrlUrlType, RelationUrlUrlTypeAdmin)

from django.contrib import admin
from catalog.models import EntityShow, EntityShowType, \
    EntityProduction, EntityProductionType, \
    EntitySeason, \
    EntityOrganity, EntityOrganityType, EntityOrganityAlias, EntityOrganityAliasType, \
    EntityWork, EntityWorkType, EntityWorkAlias, EntityWorkAliasType, \
    EntityCharacter, EntityCharacterType, EntityCharacterAlias, EntityCharacterAliasType, \
    EntityGenre, EntityGenreType, EntityGenreAlias, EntityGenreAliasType, \
    EntityUrl, EntityUrlType, \
    RelationShowShow, RelationShowShowType, \
    RelationShowProduction, RelationShowProductionType, \
    RelationShowOrganity, RelationShowOrganityType, \
    RelationShowWork, RelationShowWorkType, \
    RelationShowCharacter, RelationShowCharacterType, \
    RelationShowGenre, RelationShowGenreType, \
    RelationShowUrl, RelationShowUrlType, \
    RelationProductionProduction, RelationProductionProductionType, \
    RelationProductionOrganity, RelationProductionOrganityType, \
    RelationProductionWork, RelationProductionWorkType, \
    RelationProductionCharacter, RelationProductionCharacterType, \
    RelationProductionGenre, RelationProductionGenreType, \
    RelationProductionUrl, RelationProductionUrlType, \
    RelationOrganityOrganity, RelationOrganityOrganityType, \
    RelationOrganityWork, RelationOrganityWorkType, \
    RelationOrganityCharacter, RelationOrganityCharacterType, \
    RelationOrganityGenre, RelationOrganityGenreType, \
    RelationOrganityUrl, RelationOrganityUrlType, \
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

# relations
class RelationShowShowAdmin(admin.ModelAdmin):
    pass


class RelationShowShowTypeAdmin(admin.ModelAdmin):
    pass


class RelationShowProductionAdmin(admin.ModelAdmin):
    pass


class RelationShowProductionTypeAdmin(admin.ModelAdmin):
    pass


class RelationShowOrganityAdmin(admin.ModelAdmin):
    pass


class RelationShowOrganityTypeAdmin(admin.ModelAdmin):
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


class RelationProductionProductionAdmin(admin.ModelAdmin):
    pass


class RelationProductionProductionTypeAdmin(admin.ModelAdmin):
    pass


class RelationProductionOrganityAdmin(admin.ModelAdmin):
    pass


class RelationProductionOrganityTypeAdmin(admin.ModelAdmin):
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


class RelationOrganityOrganityAdmin(admin.ModelAdmin):
    pass


class RelationOrganityOrganityTypeAdmin(admin.ModelAdmin):
    pass


class RelationOrganityWorkAdmin(admin.ModelAdmin):
    pass


class RelationOrganityWorkTypeAdmin(admin.ModelAdmin):
    pass


class RelationOrganityCharacterAdmin(admin.ModelAdmin):
    pass


class RelationOrganityCharacterTypeAdmin(admin.ModelAdmin):
    pass


class RelationOrganityGenreAdmin(admin.ModelAdmin):
    pass


class RelationOrganityGenreTypeAdmin(admin.ModelAdmin):
    pass


class RelationOrganityUrlAdmin(admin.ModelAdmin):
    pass


class RelationOrganityUrlTypeAdmin(admin.ModelAdmin):
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


class EntityProductionAdmin(admin.ModelAdmin):
    pass


class EntityProductionTypeAdmin(admin.ModelAdmin):
    pass


class EntitySeasonAdmin(admin.ModelAdmin):
    pass


class EntityOrganityAdmin(admin.ModelAdmin):
    list_filter = ('organity_type',)


class EntityOrganityTypeAdmin(admin.ModelAdmin):
    pass


class EntityOrganityAliasAdmin(admin.ModelAdmin):
    pass


class EntityOrganityAliasTypeAdmin(admin.ModelAdmin):
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

# productions
admin.site.register(EntityProduction, EntityProductionAdmin)
admin.site.register(EntityProductionType, EntityProductionTypeAdmin)

# seasons
admin.site.register(EntitySeason, EntitySeasonAdmin)

# organisations
admin.site.register(EntityOrganity, EntityOrganityAdmin)
admin.site.register(EntityOrganityType, EntityOrganityTypeAdmin)
admin.site.register(EntityOrganityAlias, EntityOrganityAliasAdmin)
admin.site.register(EntityOrganityAliasType, EntityOrganityAliasTypeAdmin)

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
admin.site.register(RelationShowProduction, RelationShowProductionAdmin)
admin.site.register(RelationShowProductionType, RelationShowProductionTypeAdmin)
admin.site.register(RelationShowOrganity, RelationShowOrganityAdmin)
admin.site.register(RelationShowOrganityType, RelationShowOrganityTypeAdmin)
admin.site.register(RelationShowWork, RelationShowWorkAdmin)
admin.site.register(RelationShowWorkType, RelationShowWorkTypeAdmin)
admin.site.register(RelationShowCharacter, RelationShowCharacterAdmin)
admin.site.register(RelationShowCharacterType, RelationShowCharacterTypeAdmin)
admin.site.register(RelationShowGenre, RelationShowGenreAdmin)
admin.site.register(RelationShowGenreType, RelationShowGenreTypeAdmin)
admin.site.register(RelationShowUrl, RelationShowUrlAdmin)
admin.site.register(RelationShowUrlType, RelationShowUrlTypeAdmin)

admin.site.register(RelationProductionProduction, RelationProductionProductionAdmin)
admin.site.register(RelationProductionProductionType, RelationProductionProductionTypeAdmin)
admin.site.register(RelationProductionOrganity, RelationProductionOrganityAdmin)
admin.site.register(RelationProductionOrganityType, RelationProductionOrganityTypeAdmin)
admin.site.register(RelationProductionWork, RelationProductionWorkAdmin)
admin.site.register(RelationProductionWorkType, RelationProductionWorkTypeAdmin)
admin.site.register(RelationProductionCharacter, RelationProductionCharacterAdmin)
admin.site.register(RelationProductionCharacterType, RelationProductionCharacterTypeAdmin)
admin.site.register(RelationProductionGenre, RelationProductionGenreAdmin)
admin.site.register(RelationProductionGenreType, RelationProductionGenreTypeAdmin)
admin.site.register(RelationProductionUrl, RelationProductionUrlAdmin)
admin.site.register(RelationProductionUrlType, RelationProductionUrlTypeAdmin)
admin.site.register(RelationOrganityOrganity, RelationOrganityOrganityAdmin)
admin.site.register(RelationOrganityOrganityType, RelationOrganityOrganityTypeAdmin)
admin.site.register(RelationOrganityWork, RelationOrganityWorkAdmin)
admin.site.register(RelationOrganityWorkType, RelationOrganityWorkTypeAdmin)
admin.site.register(RelationOrganityCharacter, RelationOrganityCharacterAdmin)
admin.site.register(RelationOrganityCharacterType, RelationOrganityCharacterTypeAdmin)
admin.site.register(RelationOrganityGenre, RelationOrganityGenreAdmin)
admin.site.register(RelationOrganityGenreType, RelationOrganityGenreTypeAdmin)
admin.site.register(RelationOrganityUrl, RelationOrganityUrlAdmin)
admin.site.register(RelationOrganityUrlType, RelationOrganityUrlTypeAdmin)
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

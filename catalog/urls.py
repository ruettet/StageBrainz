from django.urls import path
from . import views

from django.views.generic import TemplateView

from .views import EntityOrganityAutocomplete, EntityProductionAutocomplete, EntityCharacterAutocomplete, \
    RelationProductionOrganityTypeAutocomplete, EntityShowAutocomplete, RelationOrganityOrganityTypeAutocomplete, \
    RelationShowOrganityTypeAutocomplete, EntityGenreAutocomplete, EntityWorkAutocomplete, EntityUrlAutocomplete, \
    RelationOrganityWorkTypeAutocomplete, RelationOrganityCharacterTypeAutocomplete
from .models import EntityOrganity, EntityProduction, EntityCharacter, RelationProductionOrganityType, EntityShow, \
    RelationOrganityOrganityType, RelationShowOrganityType, EntityUrl, EntityGenre, EntityWork, \
    RelationOrganityWorkType, RelationOrganityCharacterType

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('data_input/', TemplateView.as_view(template_name="datainput.html"), name='datainput'),
]

urlpatterns += [
    path('', views.index, name='index'),
]

# Entities
urlpatterns += [
    path('organities/', views.EntityOrganityListView.as_view(), name='organities'),
    path('organities/<int:pk>', views.EntityOrganityDetailView.as_view(), name='organities-detail'),
    path('organities/create/', views.EntityOrganityCreate.as_view(), name='organity_create'),
    path('organities/<int:pk>/update/', views.EntityOrganityUpdate.as_view(), name='organity_update'),
    path('organities/<int:pk>/delete/', views.EntityOrganityDelete.as_view(), name='organity_delete'),
]

urlpatterns += [
    path('organityaliases/<int:pk>', views.EntityOrganityaliasDetailView.as_view(), name='organityaliases-detail'),
    path('organityaliases/create/<int:organityid>', views.EntityOrganityAliasCreate.as_view(), name='organityalias_create'),
    path('organityaliases/<int:pk>/update/', views.EntityOrganityAliasUpdate.as_view(), name='organityalias_update'),
    path('organityaliases/<int:pk>/delete/', views.EntityOrganityAliasDelete.as_view(), name='organityalias_delete'),
]

urlpatterns += [
    path('productions/', views.EntityProductionListView.as_view(), name='productions'),
    path('productions/<int:pk>', views.EntityProductionDetailView.as_view(), name='productions-detail'),
    path('productions/create/', views.EntityProductionCreate.as_view(), name='production_create'),
    path('productions/<int:pk>/update/', views.EntityProductionUpdate.as_view(), name='production_update'),
    path('productions/<int:pk>/delete/', views.EntityProductionDelete.as_view(), name='production_delete'),
]

urlpatterns += [
    path('shows/', views.EntityShowListView.as_view(), name='shows'),
    path('shows/<int:pk>', views.EntityShowDetailView.as_view(), name='shows-detail'),
    path('shows/create/', views.EntityShowCreate.as_view(), name='show_create'),
    path('shows/<int:pk>/update/', views.EntityShowUpdate.as_view(), name='show_update'),
    path('shows/<int:pk>/delete/', views.EntityShowDelete.as_view(), name='show_delete'),
]

urlpatterns += [
    path('works/', views.EntityWorkListView.as_view(), name='works'),
    path('works/<int:pk>', views.EntityWorkDetailView.as_view(), name='works-detail'),
    path('works/create/', views.EntityWorkCreate.as_view(), name='work_create'),
    path('works/<int:pk>/update/', views.EntityWorkUpdate.as_view(), name='work_update'),
    path('works/<int:pk>/delete/', views.EntityWorkDelete.as_view(), name='work_delete'),
]

urlpatterns += [
    path('characters/', views.EntityCharacterListView.as_view(), name='characters'),
    path('characters/<int:pk>', views.EntityCharacterDetailView.as_view(), name='characters-detail'),
    path('characters/create/', views.EntityCharacterCreate.as_view(), name='character_create'),
    path('characters/<int:pk>/update/', views.EntityCharacterUpdate.as_view(), name='character_update'),
    path('characters/<int:pk>/delete/', views.EntityCharacterDelete.as_view(), name='character_delete'),
]

urlpatterns += [
    path('genres/', views.EntityGenreListView.as_view(), name='genres'),
    path('genres/<int:pk>', views.EntityGenreDetailView.as_view(), name='genres-detail'),
    path('genres/create/', views.EntityGenreCreate.as_view(), name='genre_create'),
    path('genres/<int:pk>/update/', views.EntityGenreUpdate.as_view(), name='genre_update'),
    path('genres/<int:pk>/delete/', views.EntityGenreDelete.as_view(), name='genre_delete'),
]

urlpatterns += [
    path('urls/', views.EntityUrlListView.as_view(), name='urls'),
    path('urls/<int:pk>', views.EntityUrlDetailView.as_view(), name='url-detail'),
    path('urls/create/', views.EntityUrlCreate.as_view(), name='url_create'),
    path('urls/<int:pk>/update/', views.EntityUrlUpdate.as_view(), name='url_update'),
    path('urls/<int:pk>/delete/', views.EntityUrlDelete.as_view(), name='url_delete'),
]

# Relations
# organity organity
urlpatterns += [
    path('organity_organity/create/<int:organityid>', views.RelationOrganityOrganityCreate.as_view(), name='organity_organity_create'),
    path('organity_organity/<int:pk>/update/', views.RelationOrganityOrganityUpdate.as_view(), name='organity_organity_update'),
    path('organity_organity/<int:pk>/delete/', views.RelationOrganityOrganityDelete.as_view(), name='organity_organity_delete'),
]

# organity production
urlpatterns += [
    path('production_organity/create/<int:productionid>', views.RelationProductionOrganityCreate.as_view(), name='production_organity_create'),
    path('production_organity/<int:pk>/update/', views.RelationProductionOrganityUpdate.as_view(), name='production_organity_update'),
    path('production_organity/<int:pk>/delete/', views.RelationProductionOrganityDelete.as_view(), name='production_organity_delete'),
]

# organity show
urlpatterns += [
    path('show_organity/create/<int:showid>', views.RelationShowOrganityCreate.as_view(), name='show_organity_create'),
    path('show_organity/<int:pk>/update/', views.RelationShowOrganityUpdate.as_view(), name='show_organity_update'),
    path('show_organity/<int:pk>/delete/', views.RelationShowOrganityDelete.as_view(), name='show_organity_delete'),
]

# organity work
urlpatterns += [
    path('work_organity/create/<int:workid>', views.RelationWorkOrganityCreate.as_view(), name='work_organity_create'),
    path('work_organity/<int:pk>/update/', views.RelationWorkOrganityUpdate.as_view(), name='work_organity_update'),
    path('work_organity/<int:pk>/delete/', views.RelationWorkOrganityDelete.as_view(), name='work_organity_delete'),
]

# organity character
urlpatterns += [
    path('organity_character/create/<int:organityid>', views.RelationOrganityCharacterCreate.as_view(), name='organity_character_create'),
    path('organity_character/<int:pk>/update/', views.RelationOrganityCharacterUpdate.as_view(), name='organity_character_update'),
    path('organity_character/<int:pk>/delete/', views.RelationOrganityCharacterDelete.as_view(), name='organity_character_delete'),
]

# organity genre
urlpatterns += [
    path('organity_genre/create/<int:organityid>', views.RelationOrganityGenreCreate.as_view(), name='organity_genre_create'),
    path('organity_genre/<int:pk>/update/', views.RelationOrganityGenreUpdate.as_view(), name='organity_genre_update'),
    path('organity_genre/<int:pk>/delete/', views.RelationOrganityGenreDelete.as_view(), name='organity_genre_delete'),
]

# organity url
urlpatterns += [
    path('organity_url/create/<int:organityid>', views.RelationOrganityUrlCreate.as_view(), name='organity_url_create'),
    path('organity_url/<int:pk>/update/', views.RelationOrganityUrlUpdate.as_view(), name='organity_url_update'),
    path('organity_url/<int:pk>/delete/', views.RelationOrganityUrlDelete.as_view(), name='organity_url_delete'),
]

# production production
urlpatterns += [
    path('production_production/create/<int:productionid>', views.RelationProductionProductionCreate.as_view(), name='production_production_create'),
    path('production_production/<int:pk>/update/', views.RelationProductionProductionUpdate.as_view(), name='production_production_update'),
    path('production_production/<int:pk>/delete/', views.RelationProductionProductionDelete.as_view(), name='production_production_delete'),
]

# production show
urlpatterns += [
    path('production_show/create/<int:productionid>', views.RelationProductionShowCreate.as_view(), name='production_show_create'),
    path('production_show/<int:pk>/update/', views.RelationProductionShowUpdate.as_view(), name='production_show_update'),
    path('production_show/<int:pk>/delete/', views.RelationProductionShowDelete.as_view(), name='production_show_delete'),
]

# production work
urlpatterns += [
    path('production_work/create/<int:productionid>', views.RelationProductionWorkCreate.as_view(), name='production_work_create'),
    path('production_work/<int:pk>/update/', views.RelationProductionWorkUpdate.as_view(), name='production_work_update'),
    path('production_work/<int:pk>/delete/', views.RelationProductionWorkDelete.as_view(), name='production_work_delete'),
]

# production character
urlpatterns += [
    path('production_character/create/<int:productionid>', views.RelationProductionCharacterCreate.as_view(), name='production_character_create'),
    path('production_character/<int:pk>/update/', views.RelationProductionCharacterUpdate.as_view(), name='production_character_update'),
    path('production_character/<int:pk>/delete/', views.RelationProductionCharacterDelete.as_view(), name='production_character_delete'),
]

# production genre
urlpatterns += [
    path('production_genre/create/<int:productionid>', views.RelationProductionGenreCreate.as_view(), name='production_genre_create'),
    path('production_genre/<int:pk>/update/', views.RelationProductionGenreUpdate.as_view(), name='production_genre_update'),
    path('production_genre/<int:pk>/delete/', views.RelationProductionGenreDelete.as_view(), name='production_genre_delete'),
]

# production url
urlpatterns += [
    path('production_url/create/<int:productionid>', views.RelationProductionUrlCreate.as_view(), name='production_url_create'),
    path('production_url/<int:pk>/update/', views.RelationProductionUrlUpdate.as_view(), name='production_url_update'),
    path('production_url/<int:pk>/delete/', views.RelationProductionUrlDelete.as_view(), name='production_url_delete'),
]

# show show
urlpatterns += [
    path('show_show/create/<int:showid>', views.RelationShowShowCreate.as_view(), name='show_show_create'),
    path('show_show/<int:pk>/update/', views.RelationShowShowUpdate.as_view(), name='show_show_update'),
    path('show_show/<int:pk>/delete/', views.RelationShowShowDelete.as_view(), name='show_show_delete'),
]

# show work
urlpatterns += [
    path('show_work/create/<int:showid>', views.RelationShowWorkCreate.as_view(), name='show_work_create'),
    path('show_work/<int:pk>/update/', views.RelationShowWorkUpdate.as_view(), name='show_work_update'),
    path('show_work/<int:pk>/delete/', views.RelationShowWorkDelete.as_view(), name='show_work_delete'),
]

# show character
urlpatterns += [
    path('show_character/create/<int:showid>', views.RelationShowCharacterCreate.as_view(), name='show_character_create'),
    path('show_character/<int:pk>/update/', views.RelationShowCharacterUpdate.as_view(), name='show_character_update'),
    path('show_character/<int:pk>/delete/', views.RelationShowCharacterDelete.as_view(), name='show_character_delete'),
]

# show genre
urlpatterns += [
    path('show_genre/create/<int:showid>', views.RelationShowGenreCreate.as_view(), name='show_genre_create'),
    path('show_genre/<int:pk>/update/', views.RelationShowGenreUpdate.as_view(), name='show_genre_update'),
    path('show_genre/<int:pk>/delete/', views.RelationShowGenreDelete.as_view(), name='show_genre_delete'),
]

# show url
urlpatterns += [
    path('show_url/create/<int:showid>', views.RelationShowUrlCreate.as_view(), name='show_url_create'),
    path('show_url/<int:pk>/update/', views.RelationShowUrlUpdate.as_view(), name='show_url_update'),
    path('show_url/<int:pk>/delete/', views.RelationShowUrlDelete.as_view(), name='show_url_delete'),
]

# work work
urlpatterns += [
    path('work_work/create/<int:workid>', views.RelationWorkWorkCreate.as_view(), name='work_work_create'),
    path('work_work/<int:pk>/update/', views.RelationWorkWorkUpdate.as_view(), name='work_work_update'),
    path('work_work/<int:pk>/delete/', views.RelationWorkWorkDelete.as_view(), name='work_work_delete'),
]

# work character
urlpatterns += [
    path('work_character/create/<int:workid>', views.RelationWorkCharacterCreate.as_view(), name='work_character_create'),
    path('work_character/<int:pk>/update/', views.RelationWorkCharacterUpdate.as_view(), name='work_character_update'),
    path('work_character/<int:pk>/delete/', views.RelationWorkCharacterDelete.as_view(), name='work_character_delete'),
]

# work genre
urlpatterns += [
    path('work_genre/create/<int:workid>', views.RelationWorkGenreCreate.as_view(), name='work_genre_create'),
    path('work_genre/<int:pk>/update/', views.RelationWorkGenreUpdate.as_view(), name='work_genre_update'),
    path('work_genre/<int:pk>/delete/', views.RelationWorkGenreDelete.as_view(), name='work_genre_delete'),
]

# work url
urlpatterns += [
    path('work_url/create/<int:workid>', views.RelationWorkUrlCreate.as_view(), name='work_url_create'),
    path('work_url/<int:pk>/update/', views.RelationWorkUrlUpdate.as_view(), name='work_url_update'),
    path('work_url/<int:pk>/delete/', views.RelationWorkUrlDelete.as_view(), name='work_url_delete'),
]

# character character
urlpatterns += [
    path('character_character/create/<int:characterid>', views.RelationCharacterCharacterCreate.as_view(), name='character_character_create'),
    path('character_character/<int:pk>/update/', views.RelationCharacterCharacterUpdate.as_view(), name='character_character_update'),
    path('character_character/<int:pk>/delete/', views.RelationCharacterCharacterDelete.as_view(), name='character_character_delete'),
]

# character genre
urlpatterns += [
    path('character_genre/create/<int:characterid>', views.RelationCharacterGenreCreate.as_view(), name='character_genre_create'),
    path('character_genre/<int:pk>/update/', views.RelationCharacterGenreUpdate.as_view(), name='character_genre_update'),
    path('character_genre/<int:pk>/delete/', views.RelationCharacterGenreDelete.as_view(), name='character_genre_delete'),
]

# character url
urlpatterns += [
    path('character_url/create/<int:characterid>', views.RelationCharacterUrlCreate.as_view(), name='character_url_create'),
    path('character_url/<int:pk>/update/', views.RelationCharacterUrlUpdate.as_view(), name='character_url_update'),
    path('character_url/<int:pk>/delete/', views.RelationCharacterUrlDelete.as_view(), name='character_curl_delete'),
]

# genre genre
urlpatterns += [
    path('genre_genre/create/<int:genreid>', views.RelationGenreGenreCreate.as_view(), name='genre_genre_create'),
    path('genre_genre/<int:pk>/update/', views.RelationGenreGenreUpdate.as_view(), name='genre_genre_update'),
    path('genre_genre/<int:pk>/delete/', views.RelationGenreGenreDelete.as_view(), name='genre_genre_delete'),
]

# genre url
urlpatterns += [
    path('genre_url/create/<int:genreid>', views.RelationGenreUrlCreate.as_view(), name='genre_url_create'),
    path('genre_url/<int:pk>/update/', views.RelationGenreUrlUpdate.as_view(), name='genre_url_update'),
    path('genre_url<int:pk>/delete/', views.RelationGenreUrlDelete.as_view(), name='genre_url_delete'),
]

# genre url
urlpatterns += [
    path('url_url/create/<int:urlid>', views.RelationUrlUrlCreate.as_view(), name='url_url_create'),
    path('url_url/<int:pk>/update/', views.RelationUrlUrlUpdate.as_view(), name='url_url_update'),
    path('url_url<int:pk>/delete/', views.RelationUrlUrlDelete.as_view(), name='url_url_delete'),
]

urlpatterns += [
    path('organity-autocomplete/', EntityOrganityAutocomplete.as_view(model=EntityOrganity, create_field='name'), name='organity_autocomplete'),
    path('production-autocomplete/', EntityProductionAutocomplete.as_view(model=EntityProduction, create_field='name'), name='production_autocomplete'),
    path('character-autocomplete/', EntityCharacterAutocomplete.as_view(model=EntityCharacter, create_field='name'), name='character_autocomplete'),
    path('show-autocomplete/', EntityShowAutocomplete.as_view(model=EntityShow, create_field='name'), name='show_autocomplete'),
    path('work-autocomplete/', EntityWorkAutocomplete.as_view(model=EntityWork, create_field='name'), name='work_autocomplete'),
    path('genre-autocomplete/', EntityGenreAutocomplete.as_view(model=EntityGenre), name='genre_autocomplete'),
    path('url-autocomplete/', EntityUrlAutocomplete.as_view(model=EntityUrl, create_field='name'), name='url_autocomplete'),
    path('relationorganityorganitytype-autocomplete/', RelationOrganityOrganityTypeAutocomplete.as_view(model=RelationOrganityOrganityType), name='relationorganityorganitytype_autocomplete'),
    path('relationproductionorganitytype-autocomplete/', RelationProductionOrganityTypeAutocomplete.as_view(model=RelationProductionOrganityType), name='relationproductionorganitytype_autocomplete'),
    path('relationshoworganitytype-autocomplete/', RelationShowOrganityTypeAutocomplete.as_view(model=RelationShowOrganityType), name='relationshoworganitytype_autocomplete'),
    path('relationorganityworktype-autocomplete/', RelationOrganityWorkTypeAutocomplete.as_view(model=RelationOrganityWorkType), name='relationorganityworktype_autocomplete'),
    path('relationorganitycharactertype-autocomplete/', RelationOrganityCharacterTypeAutocomplete.as_view(model=RelationOrganityCharacterType), name='relationorganitycharactertype_autocomplete'),
]
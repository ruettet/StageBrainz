from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.utils.translation import ugettext_lazy as _

from catalog.models import EntityOrganity, EntityOrganityAlias, EntityProduction, EntityShow, EntityWork, EntityCharacter, EntityGenre, EntityUrl
from catalog.models import \
    RelationOrganityOrganity, RelationOrganityCharacter, RelationOrganityGenre, RelationProductionOrganity, RelationShowOrganity, RelationOrganityUrl, RelationOrganityWork, \
    RelationProductionProduction, RelationShowProduction, RelationProductionGenre, RelationProductionWork, RelationProductionCharacter, RelationProductionUrl, \
    RelationShowShow, RelationShowCharacter, RelationShowGenre, RelationShowUrl, RelationShowWork, \
    RelationWorkWork, RelationWorkCharacter, RelationWorkGenre, RelationWorkUrl, \
    RelationCharacterCharacter, RelationCharacterGenre, RelationCharacterUrl, \
    RelationGenreGenre, RelationGenreUrl, \
    RelationUrlUrl


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_orgs = EntityOrganity.objects.all().count()
    num_prods = EntityProduction.objects.count()
    num_shows = EntityShow.objects.count()
    num_works = EntityWork.objects.count()
    num_chars = EntityCharacter.objects.count()

    context = {
        'num_orgs': num_orgs,
        'num_prods': num_prods,
        'num_shows': num_shows,
        'num_works': num_works,
        'num_chars': num_chars
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


# Organities
class EntityOrganityListView(generic.ListView):
    model = EntityOrganity


class EntityOrganityDetailView(generic.DetailView):
    model = EntityOrganity


class EntityOrganityCreate(CreateView):
    model = EntityOrganity
    fields = '__all__'


class EntityOrganityUpdate(UpdateView):
    model = EntityOrganity
    fields = '__all__'


class EntityOrganityDelete(DeleteView):
    model = EntityOrganity
    success_url = reverse_lazy('organities')


# Organitie aliasas
class EntityOrganityaliasDetailView(generic.DetailView):
    model = EntityOrganityAlias


class EntityOrganityAliasCreate(CreateView):
    model = EntityOrganityAlias
    fields = '__all__'

    def get_initial(self):
        organity = get_object_or_404(EntityOrganity, pk=self.kwargs.get("organityid"))
        return {
            'super_entity': organity,
        }

    def get_success_url(self):
        return reverse_lazy('organities-detail', kwargs={"pk": self.kwargs.get("organityid")})


class EntityOrganityAliasUpdate(UpdateView):
    model = EntityOrganityAlias
    fields = '__all__'


class EntityOrganityAliasDelete(DeleteView):
    model = EntityOrganityAlias
    success_url = reverse_lazy('organities')


# Productions
class EntityProductionListView(generic.ListView):
    model = EntityProduction


class EntityProductionDetailView(generic.DetailView):
    model = EntityProduction


class EntityProductionCreate(CreateView):
    model = EntityProduction
    fields = ['name', 'sort_name', 'disambiguation', 'entity_type', 'season']


class EntityProductionUpdate(UpdateView):
    model = EntityProduction
    fields = ['name', 'sort_name', 'disambiguation', 'entity_type', 'season']


class EntityProductionDelete(DeleteView):
    model = EntityProduction
    success_url = reverse_lazy('productions')


# Shows
class EntityShowListView(generic.ListView):
    model = EntityShow


class EntityShowDetailView(generic.DetailView):
    model = EntityShow


class EntityShowCreate(CreateView):
    model = EntityShow
    fields = '__all__'


class EntityShowUpdate(UpdateView):
    model = EntityShow
    fields = '__all__'


class EntityShowDelete(DeleteView):
    model = EntityShow
    success_url = reverse_lazy('shows')


# Works
class EntityWorkListView(generic.ListView):
    model = EntityWork


class EntityWorkDetailView(generic.DetailView):
    model = EntityWork


class EntityWorkCreate(CreateView):
    model = EntityWork
    fields = '__all__'


class EntityWorkUpdate(UpdateView):
    model = EntityWork
    fields = '__all__'


class EntityWorkDelete(DeleteView):
    model = EntityWork
    success_url = reverse_lazy('works')


# Characters
class EntityCharacterListView(generic.ListView):
    model = EntityCharacter


class EntityCharacterDetailView(generic.DetailView):
    model = EntityCharacter


class EntityCharacterCreate(CreateView):
    model = EntityCharacter
    fields = '__all__'


class EntityCharacterUpdate(UpdateView):
    model = EntityCharacter
    fields = '__all__'


class EntityCharacterDelete(DeleteView):
    model = EntityCharacter
    success_url = reverse_lazy('characters')


# Genres
class EntityGenreListView(generic.ListView):
    model = EntityGenre


class EntityGenreDetailView(generic.DetailView):
    model = EntityGenre


class EntityGenreCreate(CreateView):
    model = EntityGenre
    fields = '__all__'


class EntityGenreUpdate(UpdateView):
    model = EntityGenre
    fields = '__all__'


class EntityGenreDelete(DeleteView):
    model = EntityGenre
    success_url = reverse_lazy('genres')


# Urls
class EntityUrlListView(generic.ListView):
    model = EntityUrl


class EntityUrlDetailView(generic.DetailView):
    model = EntityUrl


class EntityUrlCreate(CreateView):
    model = EntityUrl
    fields = '__all__'


class EntityUrlUpdate(UpdateView):
    model = EntityUrl
    fields = '__all__'


class EntityUrlDelete(DeleteView):
    model = EntityUrl
    success_url = reverse_lazy('urls')


# Relations
# Organity to Organity
class RelationOrganityOrganityCreate(CreateView):
    model = RelationOrganityOrganity
    fields = '__all__'

    def get_initial(self):
        organity = get_object_or_404(EntityOrganity, pk=self.kwargs.get("organityid"))
        return {
            'entity_a': organity,
        }

    def get_success_url(self):
        return reverse_lazy('organities-detail', kwargs={"pk": self.kwargs.get("organityid")})


class RelationOrganityOrganityUpdate(UpdateView):
    model = RelationOrganityOrganity
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityOrganity, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


class RelationOrganityOrganityDelete(DeleteView):
    model = RelationOrganityOrganity

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityOrganity, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


# Organity to Production
class RelationProductionOrganityCreate(CreateView):
    model = RelationProductionOrganity
    fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as', 'context_of_character', 'context_of_character_str', 'highlighted_relation', 'begin_date', 'end_date']

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionOrganityUpdate(UpdateView):
    model = RelationProductionOrganity
    fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as', 'context_of_character', 'context_of_character_str', 'highlighted_relation', 'begin_date', 'end_date']

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionOrganity, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionOrganityDelete(DeleteView):
    model = RelationProductionOrganity

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionOrganity, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Organity to show
class RelationShowOrganityCreate(CreateView):
    model = RelationShowOrganity
    fields = '__all__'

    def get_initial(self):
        show = get_object_or_404(EntityShow, pk=self.kwargs.get("showid"))
        return {
            'entity_a': show,
        }

    def get_success_url(self):
        return reverse_lazy('shows-detail', kwargs={"pk": self.kwargs.get("showid")})


class RelationShowOrganityUpdate(UpdateView):
    model = RelationShowOrganity
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationShowProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


class RelationShowOrganityDelete(DeleteView):
    model = RelationShowOrganity

    def get_success_url(self):
        relation = get_object_or_404(RelationShowProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


# Organity to work
class RelationWorkOrganityCreate(CreateView):
    model = RelationOrganityWork
    fields = '__all__'

    def get_initial(self):
        work = get_object_or_404(EntityWork, pk=self.kwargs.get("workid"))
        return {
            'entity_b': work,
        }

    def get_success_url(self):
        return reverse_lazy('works-detail', kwargs={"pk": self.kwargs.get("workid")})


class RelationWorkOrganityUpdate(UpdateView):
    model = RelationOrganityWork
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_b.id})


class RelationWorkOrganityDelete(DeleteView):
    model = RelationOrganityWork

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_b.id})


# Organity to character
class RelationOrganityCharacterCreate(CreateView):
    model = RelationOrganityCharacter
    fields = '__all__'

    def get_initial(self):
        organity = get_object_or_404(EntityOrganity, pk=self.kwargs.get("organityid"))
        return {
            'entity_a': organity,
        }

    def get_success_url(self):
        return reverse_lazy('organities-detail', kwargs={"pk": self.kwargs.get("organityid")})


class RelationOrganityCharacterUpdate(UpdateView):
    model = RelationOrganityCharacter
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('organitiess-detail', kwargs={"pk": relation.entity_a.id})


class RelationOrganityCharacterDelete(DeleteView):
    model = RelationOrganityCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


# Organity to genre
class RelationOrganityGenreCreate(CreateView):
    model = RelationOrganityGenre
    fields = '__all__'

    def get_initial(self):
        organity = get_object_or_404(EntityOrganity, pk=self.kwargs.get("organityid"))
        return {
            'entity_a': organity,
        }

    def get_success_url(self):
        return reverse_lazy('organities-detail', kwargs={"pk": self.kwargs.get("organityid")})


class RelationOrganityGenreUpdate(UpdateView):
    model = RelationOrganityGenre
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('organitiess-detail', kwargs={"pk": relation.entity_a.id})


class RelationOrganityGenreDelete(DeleteView):
    model = RelationOrganityGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


# Organity to url
class RelationOrganityUrlCreate(CreateView):
    model = RelationOrganityUrl
    fields = '__all__'

    def get_initial(self):
        organity = get_object_or_404(EntityOrganity, pk=self.kwargs.get("organityid"))
        return {
            'entity_a': organity,
        }

    def get_success_url(self):
        return reverse_lazy('organities-detail', kwargs={"pk": self.kwargs.get("organityid")})


class RelationOrganityUrlUpdate(UpdateView):
    model = RelationOrganityUrl
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


class RelationOrganityUrlDelete(DeleteView):
    model = RelationOrganityUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


# Production to production
class RelationProductionProductionCreate(CreateView):
    model = RelationProductionProduction
    fields = '__all__'

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionProductionUpdate(UpdateView):
    model = RelationProductionProduction
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionProductionDelete(DeleteView):
    model = RelationProductionProduction

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Production to Show
class RelationProductionShowCreate(CreateView):
    model = RelationShowProduction
    fields = '__all__'

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_b': production,
            'inverted_relation': True
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionShowUpdate(UpdateView):
    model = RelationShowProduction
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationShowProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_b.id})


class RelationProductionShowDelete(DeleteView):
    model = RelationShowProduction

    def get_success_url(self):
        relation = get_object_or_404(RelationShowProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_b.id})


# Production to work
class RelationProductionWorkCreate(CreateView):
    model = RelationProductionWork
    fields = '__all__'

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionWorkUpdate(UpdateView):
    model = RelationProductionWork
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionWorkDelete(DeleteView):
    model = RelationProductionWork

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Production to character
class RelationProductionCharacterCreate(CreateView):
    model = RelationProductionCharacter
    fields = '__all__'

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionCharacterUpdate(UpdateView):
    model = RelationProductionCharacter
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionCharacterDelete(DeleteView):
    model = RelationProductionCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Production to genre
class RelationProductionGenreCreate(CreateView):
    model = RelationProductionGenre
    fields = '__all__'

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionGenreUpdate(UpdateView):
    model = RelationProductionGenre
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionGenreDelete(DeleteView):
    model = RelationProductionGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Production to url
class RelationProductionUrlCreate(CreateView):
    model = RelationProductionUrl
    fields = '__all__'

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionUrlUpdate(UpdateView):
    model = RelationProductionUrl
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionUrlDelete(DeleteView):
    model = RelationProductionUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Show to show
class RelationShowShowCreate(CreateView):
    model = RelationShowShow
    fields = '__all__'

    def get_initial(self):
        show = get_object_or_404(EntityShow, pk=self.kwargs.get("showid"))
        return {
            'entity_a': show,
        }

    def get_success_url(self):
        return reverse_lazy('shows-detail', kwargs={"pk": self.kwargs.get("showid")})


class RelationShowShowUpdate(UpdateView):
    model = RelationShowShow
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationShowShow, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


class RelationShowShowDelete(DeleteView):
    model = RelationShowShow

    def get_success_url(self):
        relation = get_object_or_404(RelationShowShow, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


# Show to work
class RelationShowWorkCreate(CreateView):
    model = RelationShowWork
    fields = '__all__'

    def get_initial(self):
        show = get_object_or_404(EntityShow, pk=self.kwargs.get("showid"))
        return {
            'entity_a': show,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("showid")})


class RelationShowWorkUpdate(UpdateView):
    model = RelationShowWork
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationShowWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


class RelationShowWorkDelete(DeleteView):
    model = RelationShowWork

    def get_success_url(self):
        relation = get_object_or_404(RelationShowWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


# Show to character
class RelationShowCharacterCreate(CreateView):
    model = RelationShowCharacter
    fields = '__all__'

    def get_initial(self):
        show = get_object_or_404(EntityShow, pk=self.kwargs.get("showid"))
        return {
            'entity_a': show,
        }

    def get_success_url(self):
        return reverse_lazy('shows-detail', kwargs={"pk": self.kwargs.get("showid")})


class RelationShowCharacterUpdate(UpdateView):
    model = RelationShowCharacter
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationShowCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


class RelationShowCharacterDelete(DeleteView):
    model = RelationShowCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationShowCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


# Show to genre
class RelationShowGenreCreate(CreateView):
    model = RelationShowGenre
    fields = '__all__'

    def get_initial(self):
        show = get_object_or_404(EntityShow, pk=self.kwargs.get("showid"))
        return {
            'entity_a': show,
        }

    def get_success_url(self):
        return reverse_lazy('shows-detail', kwargs={"pk": self.kwargs.get("showid")})


class RelationShowGenreUpdate(UpdateView):
    model = RelationShowGenre
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationShowGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


class RelationShowGenreDelete(DeleteView):
    model = RelationShowGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationShowGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


# Show to url
class RelationShowUrlCreate(CreateView):
    model = RelationShowUrl
    fields = '__all__'

    def get_initial(self):
        show = get_object_or_404(EntityShow, pk=self.kwargs.get("showid"))
        return {
            'entity_a': show,
        }

    def get_success_url(self):
        return reverse_lazy('shows-detail', kwargs={"pk": self.kwargs.get("showid")})


class RelationShowUrlUpdate(UpdateView):
    model = RelationShowUrl
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationShowUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


class RelationShowUrlDelete(DeleteView):
    model = RelationShowUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationShowUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


# Work to work
class RelationWorkWorkCreate(CreateView):
    model = RelationWorkWork
    fields = '__all__'

    def get_initial(self):
        work = get_object_or_404(EntityWork, pk=self.kwargs.get("workid"))
        return {
            'entity_a': work,
        }

    def get_success_url(self):
        return reverse_lazy('works-detail', kwargs={"pk": self.kwargs.get("workid")})


class RelationWorkWorkUpdate(UpdateView):
    model = RelationWorkWork
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


class RelationWorkWorkDelete(DeleteView):
    model = RelationWorkWork

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


# work to character
class RelationWorkCharacterCreate(CreateView):
    model = RelationWorkCharacter
    fields = '__all__'

    def get_initial(self):
        work = get_object_or_404(EntityWork, pk=self.kwargs.get("workid"))
        return {
            'entity_a': work,
        }

    def get_success_url(self):
        return reverse_lazy('works-detail', kwargs={"pk": self.kwargs.get("workid")})


class RelationWorkCharacterUpdate(UpdateView):
    model = RelationWorkCharacter
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


class RelationWorkCharacterDelete(DeleteView):
    model = RelationWorkCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


# Work to genre
class RelationWorkGenreCreate(CreateView):
    model = RelationWorkGenre
    fields = '__all__'

    def get_initial(self):
        work = get_object_or_404(EntityWork, pk=self.kwargs.get("workid"))
        return {
            'entity_a': work,
        }

    def get_success_url(self):
        return reverse_lazy('works-detail', kwargs={"pk": self.kwargs.get("workid")})


class RelationWorkGenreUpdate(UpdateView):
    model = RelationWorkGenre
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


class RelationWorkGenreDelete(DeleteView):
    model = RelationWorkGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


# work to url
class RelationWorkUrlCreate(CreateView):
    model = RelationWorkUrl
    fields = '__all__'

    def get_initial(self):
        work = get_object_or_404(EntityWork, pk=self.kwargs.get("workid"))
        return {
            'entity_a': work,
        }

    def get_success_url(self):
        return reverse_lazy('works-detail', kwargs={"pk": self.kwargs.get("workid")})


class RelationWorkUrlUpdate(UpdateView):
    model = RelationWorkUrl
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


class RelationWorkUrlDelete(DeleteView):
    model = RelationWorkUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


# Character to character
class RelationCharacterCharacterCreate(CreateView):
    model = RelationCharacterCharacter
    fields = '__all__'

    def get_initial(self):
        character = get_object_or_404(EntityCharacter, pk=self.kwargs.get("characterid"))
        return {
            'entity_a': character,
        }

    def get_success_url(self):
        return reverse_lazy('characters-detail', kwargs={"pk": self.kwargs.get("characterid")})


class RelationCharacterCharacterUpdate(UpdateView):
    model = RelationCharacterCharacter
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


class RelationCharacterCharacterDelete(DeleteView):
    model = RelationCharacterCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


# Character to genre
class RelationCharacterGenreCreate(CreateView):
    model = RelationCharacterGenre
    fields = '__all__'

    def get_initial(self):
        character = get_object_or_404(EntityCharacter, pk=self.kwargs.get("characterid"))
        return {
            'entity_a': character,
        }

    def get_success_url(self):
        return reverse_lazy('characters-detail', kwargs={"pk": self.kwargs.get("characterid")})


class RelationCharacterGenreUpdate(UpdateView):
    model = RelationCharacterGenre
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


class RelationCharacterGenreDelete(DeleteView):
    model = RelationCharacterGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


# Character to Url
class RelationCharacterUrlCreate(CreateView):
    model = RelationCharacterUrl
    fields = '__all__'

    def get_initial(self):
        character = get_object_or_404(EntityCharacter, pk=self.kwargs.get("characterid"))
        return {
            'entity_a': character,
        }

    def get_success_url(self):
        return reverse_lazy('characters-detail', kwargs={"pk": self.kwargs.get("characterid")})


class RelationCharacterUrlUpdate(UpdateView):
    model = RelationCharacterUrl
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


class RelationCharacterUrlDelete(DeleteView):
    model = RelationCharacterUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


# Genre to genre
class RelationGenreGenreCreate(CreateView):
    model = RelationGenreGenre
    fields = '__all__'

    def get_initial(self):
        genre = get_object_or_404(EntityGenre, pk=self.kwargs.get("genreid"))
        return {
            'entity_a': genre,
        }

    def get_success_url(self):
        return reverse_lazy('genres-detail', kwargs={"pk": self.kwargs.get("genreid")})


class RelationGenreGenreUpdate(UpdateView):
    model = RelationGenreGenre
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationGenreGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('genres-detail', kwargs={"pk": relation.entity_a.id})


class RelationGenreGenreDelete(DeleteView):
    model = RelationGenreGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationGenreGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('genres-detail', kwargs={"pk": relation.entity_a.id})


# Genre to url
class RelationGenreUrlCreate(CreateView):
    model = RelationGenreUrl
    fields = '__all__'

    def get_initial(self):
        genre = get_object_or_404(EntityGenre, pk=self.kwargs.get("genreid"))
        return {
            'entity_a': genre,
        }

    def get_success_url(self):
        return reverse_lazy('genres-detail', kwargs={"pk": self.kwargs.get("genreid")})


class RelationGenreUrlUpdate(UpdateView):
    model = RelationGenreUrl
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationGenreUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('genres-detail', kwargs={"pk": relation.entity_a.id})


class RelationGenreUrlDelete(DeleteView):
    model = RelationGenreUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationGenreUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('genres-detail', kwargs={"pk": relation.entity_a.id})


# Url to url
class RelationUrlUrlCreate(CreateView):
    model = RelationUrlUrl
    fields = '__all__'

    def get_initial(self):
        url = get_object_or_404(EntityUrl, pk=self.kwargs.get("urlid"))
        return {
            'entity_a': url,
        }

    def get_success_url(self):
        return reverse_lazy('url-detail', kwargs={"pk": self.kwargs.get("urlid")})


class RelationUrlUrlUpdate(UpdateView):
    model = RelationUrlUrl
    fields = '__all__'

    def get_success_url(self):
        relation = get_object_or_404(RelationUrlUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('url-detail', kwargs={"pk": relation.entity_a.id})


class RelationUrlUrlDelete(DeleteView):
    model = RelationUrlUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationUrlUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('url-detail', kwargs={"pk": relation.entity_a.id})

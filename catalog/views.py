from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import widgets
from django import forms

from catalog.models import EntityOrganity, EntityOrganityAlias, EntityProduction, EntityShow, EntityWork, \
    EntityCharacter, EntityGenre, EntityUrl, RelationProductionProductionType, RelationShowProductionType, \
    RelationOrganityOrganity, RelationOrganityCharacter, RelationOrganityGenre, RelationProductionOrganity, \
    RelationShowOrganity, RelationOrganityUrl, RelationOrganityWork, \
    RelationProductionProduction, RelationShowProduction, RelationProductionGenre, RelationProductionWork, \
    RelationProductionCharacter, RelationProductionUrl, \
    RelationShowShow, RelationShowCharacter, RelationShowGenre, RelationShowUrl, RelationShowWork, \
    RelationWorkWork, RelationWorkCharacter, RelationWorkGenre, RelationWorkUrl, \
    RelationCharacterCharacter, RelationCharacterGenre, RelationCharacterUrl, \
    RelationGenreGenre, RelationGenreUrl, \
    RelationUrlUrl, \
    RelationOrganityOrganityType, RelationProductionOrganityType, RelationShowOrganityType, RelationOrganityWorkType, \
    RelationOrganityCharacterType, RelationOrganityGenreType, RelationProductionWorkType, \
    RelationProductionCharacterType, RelationProductionGenreType, RelationProductionUrlType, RelationShowShowType, \
    RelationShowWorkType, RelationShowCharacterType, RelationShowGenreType, RelationShowUrlType, RelationWorkWorkType, \
    RelationWorkCharacterType, RelationWorkGenreType, RelationWorkUrlType, RelationCharacterCharacterType, \
    RelationCharacterGenreType, RelationCharacterUrlType, RelationGenreGenreType, RelationGenreUrlType, \
    RelationUrlUrlType, EntityOrganityType, EntityProductionType, EntityShowType, EntityCharacterType, EntityWorkType, \
    EntityGenreType, EntityUrlType, Season, Locale

from dal import autocomplete


# Entities
class EntityOrganityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityOrganity.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityProductionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityProduction.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityShowAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityShow.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityCharacterAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityCharacter.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityWorkAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityWork.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityGenreAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityGenre.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityUrlAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityUrl.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class SeasonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Season.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class LocaleAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Locale.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


# Entity types
class EntityOrganityTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityOrganityType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityProductionTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityProductionType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityShowTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityShowType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityCharacterTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityCharacterType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityWorkTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityWorkType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityGenreTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityGenreType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class EntityUrlTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = EntityUrlType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


# Relation types
class RelationOrganityOrganityTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationOrganityOrganityType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationProductionOrganityTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationProductionOrganityType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationShowOrganityTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationShowOrganityType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationOrganityWorkTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationOrganityWorkType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationOrganityCharacterTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationOrganityCharacterType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationOrganityGenreTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationOrganityGenreType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationOrganityUrlTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationOrganityGenreType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationProductionProductionTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationProductionProductionType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationProductionWorkTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationProductionWorkType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationShowProductionTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationShowProductionType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationProductionCharacterTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationProductionCharacterType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationProductionGenreTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationProductionGenreType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationProductionUrlTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationProductionUrlType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationShowShowTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationShowShowType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationShowWorkTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationShowWorkType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationShowCharacterTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationShowCharacterType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationShowGenreTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationShowGenreType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationShowUrlTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationShowUrlType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationWorkWorkTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationWorkWorkType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationWorkCharacterTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationWorkCharacterType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationWorkGenreTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationWorkGenreType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationWorkUrlTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationWorkUrlType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationCharacterCharacterTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationCharacterCharacterType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationCharacterGenreTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationCharacterGenreType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationCharacterUrlTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationCharacterUrlType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationGenreGenreTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationGenreGenreType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationGenreUrlTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationGenreUrlType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class RelationUrlUrlTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RelationUrlUrlType.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


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
class EntityOrganityForm(forms.ModelForm):
    class Meta:
        model = EntityOrganity
        fields = ['name', 'sort_name', 'disambiguation', 'entity_type', 'entity_type_str', 'start_date', 'end_date', ]
        labels = {
            'name': 'Name',
            'sort_name': 'Sort name',
            'disambiguation': 'Disambiguation line',
            'entity_type': 'Type of organity',
            'entity_type_str': 'Type of organity (free text)',
            'start_date': 'Start of organity (YYYY-MM-DD)',
            'end_date': 'End of organity (YYYY-MM-DD)',
        }
        widgets = {
            'entity_type': autocomplete.ModelSelect2Multiple(
                url='organitytype_autocomplete'
            ),
        }


class EntityOrganityListView(generic.ListView):
    model = EntityOrganity
    paginate_by = 10


class EntityOrganityDetailView(generic.DetailView):
    model = EntityOrganity


class EntityOrganityCreate(CreateView):
    form_class = EntityOrganityForm
    model = EntityOrganity


class EntityOrganityUpdate(UpdateView):
    form_class = EntityOrganityForm
    model = EntityOrganity


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
class EntityProductionForm(forms.ModelForm):
    class Meta:
        model = EntityProduction
        fields = ['name', 'sort_name', 'disambiguation', 'season', 'entity_type', 'entity_type_str', 'start_date', 'end_date', ]
        labels = {
            'name': 'Name',
            'sort_name': 'Sort name',
            'disambiguation': 'Disambiguation line',
            'season': 'Season',
            'entity_type': 'Type of production',
            'entity_type_str': 'Type of production (free text)',
            'start_date': 'Start of production (YYYY-MM-DD)',
            'end_date': 'End of production (YYYY-MM-DD)',
        }
        widgets = {
            'entity_type': autocomplete.ModelSelect2Multiple(
                url='productiontype_autocomplete'
            ),
            'season': autocomplete.ModelSelect2(
                url='season_autocomplete'
            ),
        }


class EntityProductionListView(generic.ListView):
    model = EntityProduction
    paginate_by = 10


class EntityProductionDetailView(generic.DetailView):
    model = EntityProduction


class EntityProductionCreate(CreateView):
    form_class = EntityProductionForm
    model = EntityProduction


class EntityProductionUpdate(UpdateView):
    form_class = EntityProductionForm
    model = EntityProduction


class EntityProductionDelete(DeleteView):
    model = EntityProduction
    success_url = reverse_lazy('productions')


# Shows
class EntityShowForm(forms.ModelForm):
    class Meta:
        model = EntityShow
        fields = ['name', 'sort_name', 'disambiguation', 'when_date', 'when_time', 'entity_type', 'entity_type_str', ]
        labels = {
            'name': 'Name',
            'sort_name': 'Sort name',
            'disambiguation': 'Disambiguation line',
            'when_date': 'Date of show (YYYY-MM-DD)',
            'when_time': 'Time of show (HH:MM:SS)',
            'entity_type': 'Type of show',
            'entity_type_str': 'Type of show (free text)',

        }
        widgets = {
            'entity_type': autocomplete.ModelSelect2Multiple(
                url='showtype_autocomplete'
            ),
            'when_time': widgets.TimeInput()
        }


class EntityShowListView(generic.ListView):
    model = EntityShow
    paginate_by = 10


class EntityShowDetailView(generic.DetailView):
    model = EntityShow


class EntityShowCreate(CreateView):
    form_class = EntityShowForm
    model = EntityShow


class EntityShowUpdate(UpdateView):
    form_class = EntityShowForm
    model = EntityShow


class EntityShowDelete(DeleteView):
    model = EntityShow
    success_url = reverse_lazy('shows')


# Works
class EntityWorkForm(forms.ModelForm):
    class Meta:
        model = EntityWork
        fields = ['name', 'sort_name', 'disambiguation', 'start_date', 'entity_type', 'entity_type_str', ]
        labels = {
            'name': 'Name',
            'sort_name': 'Sort name',
            'disambiguation': 'Disambiguation line',
            'start_date': 'Date',
            'entity_type': 'Type of work',
            'entity_type_str': 'Type of work (free text)',

        }
        widgets = {
            'entity_type': autocomplete.ModelSelect2Multiple(
                url='worktype_autocomplete'
            ),
        }


class EntityWorkListView(generic.ListView):
    model = EntityWork
    paginate_by = 10


class EntityWorkDetailView(generic.DetailView):
    model = EntityWork


class EntityWorkCreate(CreateView):
    form_class = EntityWorkForm
    model = EntityWork


class EntityWorkUpdate(UpdateView):
    form_class = EntityWorkForm
    model = EntityWork


class EntityWorkDelete(DeleteView):
    model = EntityWork
    success_url = reverse_lazy('works')


# Characters
class EntityCharacterForm(forms.ModelForm):
    class Meta:
        model = EntityCharacter
        fields = ['name', 'sort_name', 'disambiguation', 'entity_type', 'entity_type_str', ]
        labels = {
            'name': 'Name',
            'sort_name': 'Sort name',
            'disambiguation': 'Disambiguation line',
            'entity_type': 'Type of character',
            'entity_type_str': 'Type of character (free text)',

        }
        widgets = {
            'entity_type': autocomplete.ModelSelect2Multiple(
                url='charactertype_autocomplete'
            ),
        }


class EntityCharacterListView(generic.ListView):
    model = EntityCharacter
    paginate_by = 10


class EntityCharacterDetailView(generic.DetailView):
    model = EntityCharacter


class EntityCharacterCreate(CreateView):
    form_class = EntityCharacterForm
    model = EntityCharacter


class EntityCharacterUpdate(UpdateView):
    form_class = EntityCharacterForm
    model = EntityCharacter


class EntityCharacterDelete(DeleteView):
    model = EntityCharacter
    success_url = reverse_lazy('characters')


# Genres
class EntityGenreListView(generic.ListView):
    model = EntityGenre
    paginate_by = 10


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
    paginate_by = 10


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
class RelationOrganityOrganityForm(forms.ModelForm):
    class Meta:
        model = RelationOrganityOrganity
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as', 'start_date', 'end_date', ]
        labels = {
            'entity_a': 'Organity (from)',
            'entity_a_credited_as': 'Organity (from) credited as',
            'relation_type': "Relation type",
            'entity_b': 'Organity (to)',
            'entity_b_credited_as': 'Organity (to) credited as',
            'start_date': 'Relation start (YYYY-MM-DD)',
            'end_date': 'Relation end (YYYY-MM-DD)',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='organity_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='organity_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationorganityorganitytype_autocomplete'
            ),
        }


class RelationOrganityOrganityCreate(CreateView):
    form_class = RelationOrganityOrganityForm
    model = RelationOrganityOrganity

    def get_initial(self):
        organity = get_object_or_404(EntityOrganity, pk=self.kwargs.get("organityid"))
        return {
            'entity_a': organity,
        }

    def get_success_url(self):
        return reverse_lazy('organities-detail', kwargs={"pk": self.kwargs.get("organityid")})


class RelationOrganityOrganityUpdate(UpdateView):
    form_class = RelationOrganityOrganityForm
    model = RelationOrganityOrganity

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityOrganity, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


class RelationOrganityOrganityDelete(DeleteView):
    model = RelationOrganityOrganity

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityOrganity, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


# Organity to Production
class RelationProductionOrganityForm(forms.ModelForm):
    class Meta:
        model = RelationProductionOrganity
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as', 'start_date', 'end_date', 'context_of_character', 'context_of_character_str', 'highlighted_relation', ]
        labels = {
            'entity_a': 'Production',
            'entity_a_credited_as': 'Production credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Organity',
            'entity_b_credited_as': 'Organity credited as',
            'start_date': 'Relation start (YYYY-MM-DD)',
            'end_date': 'Relation end (YYYY-MM-DD)',
            'context_of_character': 'Role',
            'context_of_character_str': 'Role credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='production_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='organity_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationproductionorganitytype_autocomplete'
            ),
            'context_of_character': autocomplete.ModelSelect2(
                url='character_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                }
            )
        }


class RelationProductionOrganityCreate(CreateView):
    form_class = RelationProductionOrganityForm
    model = RelationProductionOrganity

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionOrganityUpdate(UpdateView):
    form_class = RelationProductionOrganityForm
    model = RelationProductionOrganity

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionOrganity, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionOrganityDelete(DeleteView):
    model = RelationProductionOrganity

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionOrganity, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Organity to show
class RelationShowOrganityForm(forms.ModelForm):
    class Meta:
        model = RelationShowOrganity
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as', 'context_of_character', 'context_of_character_str']
        labels = {
            'entity_a': 'Show',
            'entity_a_credited_as': 'Show credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Organity',
            'entity_b_credited_as': 'Organity credited as',
            'context_of_character': 'Role',
            'context_of_character_str': 'Role credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='show_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='organity_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationshoworganitytype_autocomplete'
            ),
            'context_of_character': autocomplete.ModelSelect2(
                url='character_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                }
            )
        }


class RelationShowOrganityCreate(CreateView):
    form_class = RelationShowOrganityForm
    model = RelationShowOrganity

    def get_initial(self):
        show = get_object_or_404(EntityShow, pk=self.kwargs.get("showid"))
        return {
            'entity_a': show,
        }

    def get_success_url(self):
        return reverse_lazy('shows-detail', kwargs={"pk": self.kwargs.get("showid")})


class RelationShowOrganityUpdate(UpdateView):
    form_class = RelationShowOrganityForm
    model = RelationShowOrganity

    def get_success_url(self):
        relation = get_object_or_404(RelationShowProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


class RelationShowOrganityDelete(DeleteView):
    model = RelationShowOrganity

    def get_success_url(self):
        relation = get_object_or_404(RelationShowProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


# Organity to work
class RelationWorkOrganityForm(forms.ModelForm):
    class Meta:
        model = RelationOrganityWork
        fields = ['entity_b', 'entity_b_credited_as', 'relation_type', 'relation_name', 'entity_a', 'entity_a_credited_as', 'highlighted_relation']
        labels = {
            'entity_a': 'Organity',
            'entity_a_credited_as': 'Organity credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Work',
            'entity_b_credited_as': 'Work credited as',
            'highlighed_relation': 'Highlighted relation',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='organity_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='work_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationorganityworktype_autocomplete'
            ),
        }


class RelationWorkOrganityCreate(CreateView):
    form_class = RelationWorkOrganityForm
    model = RelationOrganityWork

    def get_initial(self):
        work = get_object_or_404(EntityWork, pk=self.kwargs.get("workid"))
        return {
            'entity_b': work,
        }

    def get_success_url(self):
        return reverse_lazy('works-detail', kwargs={"pk": self.kwargs.get("workid")})


class RelationWorkOrganityUpdate(UpdateView):
    form_class = RelationWorkOrganityForm
    model = RelationOrganityWork

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_b.id})


class RelationWorkOrganityDelete(DeleteView):
    model = RelationOrganityWork

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_b.id})


# Organity to character
class RelationOrganityCharacterForm(forms.ModelForm):
    class Meta:
        model = RelationOrganityCharacter
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as', 'start_date', 'end_date',]
        labels = {
            'entity_a': 'Organity',
            'entity_a_credited_as': 'Organity credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Character',
            'entity_b_credited_as': 'Character credited as',
            'start_date': 'Start date',
            'end_date': 'End date',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='organity_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='character_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationorganitycharactertype_autocomplete'
            ),
        }


class RelationOrganityCharacterCreate(CreateView):
    form_class = RelationOrganityCharacterForm
    model = RelationOrganityCharacter

    def get_initial(self):
        organity = get_object_or_404(EntityOrganity, pk=self.kwargs.get("organityid"))
        return {
            'entity_a': organity,
        }

    def get_success_url(self):
        return reverse_lazy('organities-detail', kwargs={"pk": self.kwargs.get("organityid")})


class RelationOrganityCharacterUpdate(UpdateView):
    form_class = RelationOrganityCharacterForm
    model = RelationOrganityCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('organitiess-detail', kwargs={"pk": relation.entity_a.id})


class RelationOrganityCharacterDelete(DeleteView):
    model = RelationOrganityCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


# Organity to genre
class RelationOrganityGenreForm(forms.ModelForm):
    class Meta:
        model = RelationOrganityGenre
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Organity',
            'entity_a_credited_as': 'Organity credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Genre',
            'entity_b_credited_as': 'Genre credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='organity_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='genre_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationorganitygenretype_autocomplete'
            ),
        }


class RelationOrganityGenreCreate(CreateView):
    form_class = RelationOrganityGenreForm
    model = RelationOrganityGenre

    def get_initial(self):
        organity = get_object_or_404(EntityOrganity, pk=self.kwargs.get("organityid"))
        return {
            'entity_a': organity,
        }

    def get_success_url(self):
        return reverse_lazy('organities-detail', kwargs={"pk": self.kwargs.get("organityid")})


class RelationOrganityGenreUpdate(UpdateView):
    form_class = RelationOrganityGenreForm
    model = RelationOrganityGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('organitiess-detail', kwargs={"pk": relation.entity_a.id})


class RelationOrganityGenreDelete(DeleteView):
    model = RelationOrganityGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


# Organity to url
class RelationOrganityUrlForm(forms.ModelForm):
    class Meta:
        model = RelationOrganityUrl
        fields = ['entity_a', 'entity_b',]
        labels = {
            'entity_a': 'Organity',
            'entity_b': 'Url',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='organity_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='url_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
        }


class RelationOrganityUrlCreate(CreateView):
    form_class = RelationOrganityUrlForm
    model = RelationOrganityUrl

    def get_initial(self):
        organity = get_object_or_404(EntityOrganity, pk=self.kwargs.get("organityid"))
        return {
            'entity_a': organity,
        }

    def get_success_url(self):
        return reverse_lazy('organities-detail', kwargs={"pk": self.kwargs.get("organityid")})


class RelationOrganityUrlUpdate(UpdateView):
    form_class = RelationOrganityUrlForm
    model = RelationOrganityUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


class RelationOrganityUrlDelete(DeleteView):
    model = RelationOrganityUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationOrganityUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('organities-detail', kwargs={"pk": relation.entity_a.id})


# Production to production
class RelationProductionProductionForm(forms.ModelForm):
    class Meta:
        model = RelationProductionProduction
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Production (from)',
            'entity_a_credited_as': 'Production (from) credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Production (to)',
            'entity_b_credited_as': 'Production (to) credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='production_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='production_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationproductionproductiontype_autocomplete'
            ),
        }


class RelationProductionProductionCreate(CreateView):
    form_class = RelationProductionProductionForm
    model = RelationProductionProduction

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionProductionUpdate(UpdateView):
    form_class = RelationProductionProductionForm
    model = RelationProductionProduction

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionProductionDelete(DeleteView):
    model = RelationProductionProduction

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Production to Show
class RelationProductionShowForm(forms.ModelForm):
    class Meta:
        model = RelationShowProduction
        fields = ['entity_b', 'entity_b_credited_as', 'relation_type', 'relation_name', 'entity_a', 'entity_a_credited_as',]
        labels = {
            'entity_a': 'Show',
            'entity_a_credited_as': 'Show credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Production',
            'entity_b_credited_as': 'Production credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='show_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='production_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationshowproductiontype_autocomplete'
            ),
        }


class RelationProductionShowCreate(CreateView):
    form_class = RelationProductionShowForm
    model = RelationShowProduction

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_b': production,
            'inverted_relation': True
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionShowUpdate(UpdateView):
    form_class = RelationProductionShowForm
    model = RelationShowProduction

    def get_success_url(self):
        relation = get_object_or_404(RelationShowProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_b.id})


class RelationProductionShowDelete(DeleteView):
    model = RelationShowProduction

    def get_success_url(self):
        relation = get_object_or_404(RelationShowProduction, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_b.id})


# Production to work
class RelationProductionWorkForm(forms.ModelForm):
    class Meta:
        model = RelationProductionWork
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Production',
            'entity_a_credited_as': 'Production credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Work',
            'entity_b_credited_as': 'Work credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='production_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='work_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationproductionworktype_autocomplete'
            ),
        }


class RelationProductionWorkCreate(CreateView):
    form_class = RelationProductionWorkForm
    model = RelationProductionWork

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionWorkUpdate(UpdateView):
    form_class = RelationProductionWorkForm
    model = RelationProductionWork

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionWorkDelete(DeleteView):
    model = RelationProductionWork

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Production to character
class RelationProductionCharacterForm(forms.ModelForm):
    class Meta:
        model = RelationProductionCharacter
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Production',
            'entity_a_credited_as': 'Production credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Character',
            'entity_b_credited_as': 'Character credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='production_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='character_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationproductioncharactertype_autocomplete'
            ),
        }


class RelationProductionCharacterCreate(CreateView):
    form_class = RelationProductionCharacterForm
    model = RelationProductionCharacter

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionCharacterUpdate(UpdateView):
    form_class = RelationProductionCharacterForm
    model = RelationProductionCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionCharacterDelete(DeleteView):
    model = RelationProductionCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Production to genre
class RelationProductionGenreForm(forms.ModelForm):
    class Meta:
        model = RelationProductionGenre
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Production',
            'entity_a_credited_as': 'Production credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Genre',
            'entity_b_credited_as': 'Genre credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='production_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='genre_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationproductiongenretype_autocomplete'
            ),
        }


class RelationProductionGenreCreate(CreateView):
    form_class = RelationProductionGenreForm
    model = RelationProductionGenre

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionGenreUpdate(UpdateView):
    form_class = RelationProductionGenreForm
    model = RelationProductionGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionGenreDelete(DeleteView):
    model = RelationProductionGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Production to url
class RelationProductionUrlForm(forms.ModelForm):
    class Meta:
        model = RelationProductionUrl
        fields = ['entity_a', 'entity_a_credited_as', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Production',
            'entity_a_credited_as': 'Production credited as',
            'entity_b': 'Url',
            'entity_b_credited_as': 'Url credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='production_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='url_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationproductionurltype_autocomplete'
            ),
        }


class RelationProductionUrlCreate(CreateView):
    form_class = RelationProductionUrlForm
    model = RelationProductionUrl

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("productionid")})


class RelationProductionUrlUpdate(UpdateView):
    form_class = RelationProductionUrlForm
    model = RelationProductionUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


class RelationProductionUrlDelete(DeleteView):
    model = RelationProductionUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationProductionUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('productions-detail', kwargs={"pk": relation.entity_a.id})


# Show to show
class RelationShowShowForm(forms.ModelForm):
    class Meta:
        model = RelationShowShow
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Show (from)',
            'entity_a_credited_as': 'Show (from) credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Show (to)',
            'entity_b_credited_as': 'Show (to) credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='show_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='show_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationshowshowtype_autocomplete'
            ),
        }


class RelationShowShowCreate(CreateView):
    form_class = RelationShowShowForm
    model = RelationShowShow

    def get_initial(self):
        show = get_object_or_404(EntityShow, pk=self.kwargs.get("showid"))
        return {
            'entity_a': show,
        }

    def get_success_url(self):
        return reverse_lazy('shows-detail', kwargs={"pk": self.kwargs.get("showid")})


class RelationShowShowUpdate(UpdateView):
    form_class = RelationShowShowForm
    model = RelationShowShow

    def get_success_url(self):
        relation = get_object_or_404(RelationShowShow, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


class RelationShowShowDelete(DeleteView):
    model = RelationShowShow

    def get_success_url(self):
        relation = get_object_or_404(RelationShowShow, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


# Show to work
class RelationShowWorkForm(forms.ModelForm):
    class Meta:
        model = RelationShowWork
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Show',
            'entity_a_credited_as': 'Show credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Work',
            'entity_b_credited_as': 'Work credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='show_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='work_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationshowworktype_autocomplete'
            ),
        }


class RelationShowWorkCreate(CreateView):
    form_class = RelationShowWorkForm
    model = RelationShowWork

    def get_initial(self):
        show = get_object_or_404(EntityShow, pk=self.kwargs.get("showid"))
        return {
            'entity_a': show,
        }

    def get_success_url(self):
        return reverse_lazy('productions-detail', kwargs={"pk": self.kwargs.get("showid")})


class RelationShowWorkUpdate(UpdateView):
    form_class = RelationShowWorkForm
    model = RelationShowWork

    def get_success_url(self):
        relation = get_object_or_404(RelationShowWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


class RelationShowWorkDelete(DeleteView):
    model = RelationShowWork

    def get_success_url(self):
        relation = get_object_or_404(RelationShowWork, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


# Show to character
class RelationShowCharacterForm(forms.ModelForm):
    class Meta:
        model = RelationShowCharacter
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Show',
            'entity_a_credited_as': 'Show credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Character',
            'entity_b_credited_as': 'Character credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='show_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='character_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationshowcharactertype_autocomplete'
            ),
        }


class RelationShowCharacterCreate(CreateView):
    form_class = RelationShowCharacterForm
    model = RelationShowCharacter

    def get_initial(self):
        show = get_object_or_404(EntityShow, pk=self.kwargs.get("showid"))
        return {
            'entity_a': show,
        }

    def get_success_url(self):
        return reverse_lazy('shows-detail', kwargs={"pk": self.kwargs.get("showid")})


class RelationShowCharacterUpdate(UpdateView):
    form_class = RelationShowCharacterForm
    model = RelationShowCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationShowCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


class RelationShowCharacterDelete(DeleteView):
    model = RelationShowCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationShowCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


# Show to genre
class RelationShowGenreForm(forms.ModelForm):
    class Meta:
        model = RelationShowGenre
        fields = ['entity_a', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Show',
            'entity_b': 'Genre',
            'entity_b_credited_as': 'Character credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='show_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='genre_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
        }


class RelationShowGenreCreate(CreateView):
    form_class = RelationShowGenreForm
    model = RelationShowGenre

    def get_initial(self):
        show = get_object_or_404(EntityShow, pk=self.kwargs.get("showid"))
        return {
            'entity_a': show,
        }

    def get_success_url(self):
        return reverse_lazy('shows-detail', kwargs={"pk": self.kwargs.get("showid")})


class RelationShowGenreUpdate(UpdateView):
    form_class = RelationShowGenreForm
    model = RelationShowGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationShowGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


class RelationShowGenreDelete(DeleteView):
    model = RelationShowGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationShowGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('shows-detail', kwargs={"pk": relation.entity_a.id})


# Show to url
class RelationShowUrlForm(forms.ModelForm):
    class Meta:
        model = RelationShowUrl
        fields = ['entity_a', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Show',
            'entity_b': 'Url',
            'entity_b_credited_as': 'Url credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='show_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='url_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationshowurltype_autocomplete'
            ),
        }


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
class RelationWorkWorkForm(forms.ModelForm):
    class Meta:
        model = RelationWorkWork
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Work (from)',
            'entity_a_credited_as': 'Work (from) credited as',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Work (to)',
            'entity_b_credited_as': 'Work (to) credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='work_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='work_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationworkworktype_autocomplete'
            ),
        }


class RelationWorkWorkCreate(CreateView):
    form_class = RelationWorkWorkForm
    model = RelationWorkWork

    def get_initial(self):
        work = get_object_or_404(EntityWork, pk=self.kwargs.get("workid"))
        return {
            'entity_a': work,
        }

    def get_success_url(self):
        return reverse_lazy('works-detail', kwargs={"pk": self.kwargs.get("workid")})


class RelationWorkWorkUpdate(UpdateView):
    form_class = RelationWorkWorkForm
    model = RelationWorkWork

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
class RelationWorkGenreForm(forms.ModelForm):
    class Meta:
        model = RelationWorkGenre
        fields = ['entity_a', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Work',
            'entity_b': 'Genre',
            'entity_b_credited_as': 'Genre credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='work_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='genre_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationworkgenretype_autocomplete'
            ),
        }


class RelationWorkGenreCreate(CreateView):
    form_class = RelationWorkGenreForm
    model = RelationWorkGenre

    def get_initial(self):
        work = get_object_or_404(EntityWork, pk=self.kwargs.get("workid"))
        return {
            'entity_a': work,
        }

    def get_success_url(self):
        return reverse_lazy('works-detail', kwargs={"pk": self.kwargs.get("workid")})


class RelationWorkGenreUpdate(UpdateView):
    form_class = RelationWorkGenreForm
    model = RelationWorkGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


class RelationWorkGenreDelete(DeleteView):
    model = RelationWorkGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


# work to url
class RelationWorkUrlForm(forms.ModelForm):
    class Meta:
        model = RelationWorkUrl
        fields = ['entity_a', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Work',
            'entity_b': 'Url',
            'entity_b_credited_as': 'Url credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='work_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='url_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationworkurltype_autocomplete'
            ),
        }


class RelationWorkUrlCreate(CreateView):
    form_class = RelationWorkUrlForm
    model = RelationWorkUrl

    def get_initial(self):
        work = get_object_or_404(EntityWork, pk=self.kwargs.get("workid"))
        return {
            'entity_a': work,
        }

    def get_success_url(self):
        return reverse_lazy('works-detail', kwargs={"pk": self.kwargs.get("workid")})


class RelationWorkUrlUpdate(UpdateView):
    form_class = RelationWorkUrlForm
    model = RelationWorkUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


class RelationWorkUrlDelete(DeleteView):
    model = RelationWorkUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationWorkUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('works-detail', kwargs={"pk": relation.entity_a.id})


# Character to character
class RelationCharacterCharacterForm(forms.ModelForm):
    class Meta:
        model = RelationCharacterCharacter
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Character (from)',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Character (to)',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='character_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='character_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationcharactercharactertype_autocomplete'
            ),
        }


class RelationCharacterCharacterCreate(CreateView):
    form_class = RelationCharacterCharacterForm
    model = RelationCharacterCharacter

    def get_initial(self):
        character = get_object_or_404(EntityCharacter, pk=self.kwargs.get("characterid"))
        return {
            'entity_a': character,
        }

    def get_success_url(self):
        return reverse_lazy('characters-detail', kwargs={"pk": self.kwargs.get("characterid")})


class RelationCharacterCharacterUpdate(UpdateView):
    form_class = RelationCharacterCharacterForm
    model = RelationCharacterCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


class RelationCharacterCharacterDelete(DeleteView):
    model = RelationCharacterCharacter

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterCharacter, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


# Character to genre
class RelationCharacterGenreForm(forms.ModelForm):
    class Meta:
        model = RelationCharacterGenre
        fields = ['entity_a', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Character',
            'entity_b': 'Genre',
            'entity_b_credited_as': 'Genre credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='character_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='work_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationcharactergenretype_autocomplete'
            ),
        }


class RelationCharacterGenreCreate(CreateView):
    form_class = RelationCharacterGenreForm
    model = RelationCharacterGenre

    def get_initial(self):
        character = get_object_or_404(EntityCharacter, pk=self.kwargs.get("characterid"))
        return {
            'entity_a': character,
        }

    def get_success_url(self):
        return reverse_lazy('characters-detail', kwargs={"pk": self.kwargs.get("characterid")})


class RelationCharacterGenreUpdate(UpdateView):
    form_class = RelationCharacterGenreForm
    model = RelationCharacterGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


class RelationCharacterGenreDelete(DeleteView):
    model = RelationCharacterGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


# Character to Url
class RelationCharacterUrlForm(forms.ModelForm):
    class Meta:
        model = RelationCharacterUrl
        fields = ['entity_a', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Character',
            'entity_b': 'Url',
            'entity_b_credited_as': 'Url credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='character_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='url_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationcharacterurltype_autocomplete'
            ),
        }


class RelationCharacterUrlCreate(CreateView):
    form_class = RelationCharacterUrlForm
    model = RelationCharacterUrl

    def get_initial(self):
        character = get_object_or_404(EntityCharacter, pk=self.kwargs.get("characterid"))
        return {
            'entity_a': character,
        }

    def get_success_url(self):
        return reverse_lazy('characters-detail', kwargs={"pk": self.kwargs.get("characterid")})


class RelationCharacterUrlUpdate(UpdateView):
    form_class = RelationCharacterUrlForm
    model = RelationCharacterUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


class RelationCharacterUrlDelete(DeleteView):
    model = RelationCharacterUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationCharacterUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('characters-detail', kwargs={"pk": relation.entity_a.id})


# Genre to genre
class RelationGenreGenreForm(forms.ModelForm):
    class Meta:
        model = RelationGenreGenre
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Genre (from)',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Genre (to)',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='genre_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='genre_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationgenregenretype_autocomplete'
            ),
        }


class RelationGenreGenreCreate(CreateView):
    form_class = RelationGenreGenreForm
    model = RelationGenreGenre

    def get_initial(self):
        genre = get_object_or_404(EntityGenre, pk=self.kwargs.get("genreid"))
        return {
            'entity_a': genre,
        }

    def get_success_url(self):
        return reverse_lazy('genres-detail', kwargs={"pk": self.kwargs.get("genreid")})


class RelationGenreGenreUpdate(UpdateView):
    form_class = RelationGenreGenreForm
    model = RelationGenreGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationGenreGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('genres-detail', kwargs={"pk": relation.entity_a.id})


class RelationGenreGenreDelete(DeleteView):
    model = RelationGenreGenre

    def get_success_url(self):
        relation = get_object_or_404(RelationGenreGenre, pk=self.kwargs.get("pk"))
        return reverse_lazy('genres-detail', kwargs={"pk": relation.entity_a.id})


# Genre to url
class RelationGenreUrlForm(forms.ModelForm):
    class Meta:
        model = RelationGenreUrl
        fields = ['entity_a', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Genre',
            'entity_b': 'Url',
            'entity_b_credited_as': 'Url credited as',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='genre_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='url_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationgenreurltype_autocomplete'
            ),
        }


class RelationGenreUrlCreate(CreateView):
    form_class = RelationGenreUrlForm
    model = RelationGenreUrl

    def get_initial(self):
        genre = get_object_or_404(EntityGenre, pk=self.kwargs.get("genreid"))
        return {
            'entity_a': genre,
        }

    def get_success_url(self):
        return reverse_lazy('genres-detail', kwargs={"pk": self.kwargs.get("genreid")})


class RelationGenreUrlUpdate(UpdateView):
    form_class = RelationGenreUrlForm
    model = RelationGenreUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationGenreUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('genres-detail', kwargs={"pk": relation.entity_a.id})


class RelationGenreUrlDelete(DeleteView):
    model = RelationGenreUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationGenreUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('genres-detail', kwargs={"pk": relation.entity_a.id})


# Url to url
class RelationUrlUrlForm(forms.ModelForm):
    class Meta:
        model = RelationUrlUrl
        fields = ['entity_a', 'entity_a_credited_as', 'relation_type', 'relation_name', 'entity_b', 'entity_b_credited_as',]
        labels = {
            'entity_a': 'Url (from)',
            'relation_type': 'Relation type',
            'relation_name': 'Relation credited as',
            'entity_b': 'Url (to)',
        }
        widgets = {
            'entity_a': autocomplete.ModelSelect2(
                url='url_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'entity_b': autocomplete.ModelSelect2(
                url='url_autocomplete',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                    'data-minimum-input-length': 3,
                },
            ),
            'relation_type': autocomplete.ModelSelect2Multiple(
                url='relationurlurltype_autocomplete'
            ),
        }


class RelationUrlUrlCreate(CreateView):
    form_class = RelationUrlUrlForm
    model = RelationUrlUrl

    def get_initial(self):
        url = get_object_or_404(EntityUrl, pk=self.kwargs.get("urlid"))
        return {
            'entity_a': url,
        }

    def get_success_url(self):
        return reverse_lazy('url-detail', kwargs={"pk": self.kwargs.get("urlid")})


class RelationUrlUrlUpdate(UpdateView):
    form_class = RelationUrlUrlForm
    model = RelationUrlUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationUrlUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('url-detail', kwargs={"pk": relation.entity_a.id})


class RelationUrlUrlDelete(DeleteView):
    model = RelationUrlUrl

    def get_success_url(self):
        relation = get_object_or_404(RelationUrlUrl, pk=self.kwargs.get("pk"))
        return reverse_lazy('url-detail', kwargs={"pk": relation.entity_a.id})

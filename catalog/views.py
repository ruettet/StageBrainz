from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import EntityOrganity, EntityProduction, EntityShow
from catalog.models import RelationProductionOrganity, RelationShowProduction


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_orgs = EntityOrganity.objects.all().count()
    num_prods = EntityProduction.objects.count()

    context = {
        'num_orgs': num_orgs,
        'num_prods': num_prods
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


# Productions
class EntityProductionListView(generic.ListView):
    model = EntityProduction


class EntityProductionDetailView(generic.DetailView):
    model = EntityProduction


class EntityProductionCreate(CreateView):
    model = EntityProduction
    fields = '__all__'


class EntityProductionUpdate(UpdateView):
    model = EntityProduction
    fields = '__all__'


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


# Relations
# Production to Organity
class RelationProductionOrganityCreate(CreateView):
    model = RelationProductionOrganity
    fields = '__all__'

    def get_initial(self):
        production = get_object_or_404(EntityProduction, pk=self.kwargs.get("productionid"))
        return {
            'entity_a': production,
        }

    def get_success_url(self):
        return reverse_lazy('productions')


class RelationProductionOrganityUpdate(UpdateView):
    model = RelationProductionOrganity
    fields = '__all__'


class RelationProductionOrganityDelete(DeleteView):
    model = RelationProductionOrganity
    success_url = reverse_lazy('productions')


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
        return reverse_lazy('shows')


class RelationProductionShowUpdate(UpdateView):
    model = RelationShowProduction
    fields = '__all__'


class RelationProductionShowDelete(DeleteView):
    model = RelationShowProduction
    success_url = reverse_lazy('shows')

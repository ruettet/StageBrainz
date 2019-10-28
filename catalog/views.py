from django.shortcuts import render
from django.views import generic
from catalog.models import EntityPerson, EntityOrganisation, EntityProduction, EntityVenue


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_people = EntityPerson.objects.all().count()
    num_orgs = EntityOrganisation.objects.all().count()
    num_prods = EntityProduction.objects.count()
    num_venues = EntityVenue.objects.count()

    context = {
        'num_people': num_people,
        'num_orgs': num_orgs,
        'num_prods': num_prods,
        'num_venues': num_venues,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class EntityPersonListView(generic.ListView):
    model = EntityPerson


class EntityPersonDetailView(generic.DetailView):
    model = EntityPerson


class EntityOrganisationListView(generic.ListView):
    model = EntityOrganisation


class EntityOrganisationDetailView(generic.DetailView):
    model = EntityOrganisation


class EntityVenueListView(generic.ListView):
    model = EntityVenue


class EntityVenueDetailView(generic.DetailView):
    model = EntityVenue


class EntityProductionListView(generic.ListView):
    model = EntityProduction


class EntityProductionDetailView(generic.DetailView):
    model = EntityProduction
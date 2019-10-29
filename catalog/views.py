from django.shortcuts import render
from django.views import generic
from catalog.models import EntityOrganity, EntityProduction


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


class EntityOrganityListView(generic.ListView):
    model = EntityOrganity


class EntityOrganityDetailView(generic.DetailView):
    model = EntityOrganity


class EntityProductionListView(generic.ListView):
    model = EntityProduction


class EntityProductionDetailView(generic.DetailView):
    model = EntityProduction
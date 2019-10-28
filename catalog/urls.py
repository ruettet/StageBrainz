from django.urls import path
from . import views

urlpatterns = [

]

urlpatterns = [
    path('', views.index, name='index'),
    path('people/', views.EntityPersonListView.as_view(), name='people'),
    path('people/<int:pk>', views.EntityPersonDetailView.as_view(), name='people-detail'),
    path('organisations/', views.EntityOrganisationListView.as_view(), name='organisations'),
    path('organisations/<int:pk>', views.EntityOrganisationDetailView.as_view(), name='organisations-detail'),
    path('productions/', views.EntityProductionListView.as_view(), name='productions'),
    path('productions/<int:pk>', views.EntityProductionDetailView.as_view(), name='productions-detail'),
    path('venues/', views.EntityVenueListView.as_view(), name='venues'),
    path('venues/<int:pk>', views.EntityVenueDetailView.as_view(), name='venue-detail'),
]
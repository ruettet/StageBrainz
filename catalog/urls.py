from django.urls import path
from . import views

from django.views.generic import TemplateView

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

# Relations
urlpatterns += [
    path('production_organity/create/<int:productionid>', views.RelationProductionOrganityCreate.as_view(), name='production_organity_create'),
    path('production_organity/<int:pk>/update/', views.RelationProductionOrganityUpdate.as_view(), name='production_organity_update'),
    path('production_organity/<int:pk>/delete/', views.RelationProductionOrganityDelete.as_view(), name='production_organity_delete'),
]

urlpatterns += [
    path('production_show/create/<int:productionid>', views.RelationProductionShowCreate.as_view(), name='production_show_create'),
    path('production_show/<int:pk>/update/', views.RelationProductionShowUpdate.as_view(), name='production_show_update'),
    path('production_show/<int:pk>/delete/', views.RelationProductionShowDelete.as_view(), name='production_show_delete'),
]

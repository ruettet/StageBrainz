from django.urls import path
from . import views

urlpatterns = [

]

urlpatterns = [
    path('', views.index, name='index'),
    path('organities/', views.EntityOrganityListView.as_view(), name='organities'),
    path('organities/<int:pk>', views.EntityOrganityDetailView.as_view(), name='organities-detail'),
    path('productions/', views.EntityProductionListView.as_view(), name='productions'),
    path('productions/<int:pk>', views.EntityProductionDetailView.as_view(), name='productions-detail'),
]
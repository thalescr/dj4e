from django.urls import path

from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.CatListView.as_view(), name='cat_list'), # List cat
    path('main/create/', views.CatCreateView.as_view(), name='cat_create'), # Create cat
    path('main/<int:pk>/update', views.CatUpdateView.as_view(), name='cat_update'), # Update cat
    path('main/<int:pk>/delete', views.CatDeleteView.as_view(), name='cat_delete'), # Delete cat
    path('lookup/', views.BreedListView.as_view(), name='breed_list'), # List breeds
    path('lookup/create', views.BreedCreateView.as_view(), name='breed_create'), # Create breed
    path('lookup/<int:pk>/update', views.BreedUpdateView.as_view(), name='breed_update'), # Update breed
    path('lookup/<int:pk>/delete', views.BreedDeleteView.as_view(), name='breed_delete'), # Delete breed
]

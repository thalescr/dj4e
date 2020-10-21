from django.urls import path

from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.AutoListView.as_view(), name='auto_list'), # Autos list
    path('main/create/', views.AutoCreateView.as_view(), name='auto_create'), # Create auto
    path('main/<int:pk>/update', views.AutoUpdateView.as_view(), name='auto_update'), # Update auto
    path('main/<int:pk>/delete', views.AutoDeleteView.as_view(), name='auto_delete'), # Delete auto
    path('lookup/', views.MakeListView.as_view(), name='make_list'), # Makes list
    path('lookup/create', views.MakeCreateView.as_view(), name='make_create'), # Create make
    path('lookup/<int:pk>/update', views.MakeUpdateView.as_view(), name='make_update'), # Update make
    path('lookup/<int:pk>/delete', views.MakeDeleteView.as_view(), name='make_delete'), # Delete make
]

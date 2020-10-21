from django.urls import path

from . import views

app_name='ads'

urlpatterns = [
    path('', views.AdListView.as_view(), name='ad_list'),
    path('ad/create', views.AdCreateView.as_view(), name='ad_create'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/<int:pk>/update', views.AdUpdateView.as_view(), name='ad_update'),
    path('ad/<int:pk>/delete', views.AdDeleteView.as_view(), name='ad_delete'),
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
    path('ad/<int:pk>/comment', views.CommentCreateView.as_view(), name='ad_comment_create'),
    path('ad/<int:pk>/favorite', views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('ad/<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='ad_comment_delete'),
]
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.MemesesListView.as_view(), name='index'),
    path('memes/<slug:slug>', views.MemesDetailView.as_view(), name='meme-detail'),
    path('tag-cloud/', views.TagsCloudView.as_view(), name='tags_list'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('random/', views.RandomMemesView.as_view(), name='random_memes')
]

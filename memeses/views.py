from django.shortcuts import render

# Create your views here.
from .models import Tags, Memes
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

import random
from django.db.models import Max

import re


class MemesesListView(generic.ListView):
    model = Memes
    template_name = 'memeses_list.html'
    context_object_name = 'memeses_list'
    ordering = ['-id']
    paginate_by = 20


class MemesDetailView(generic.DetailView):
    model = Memes
    template_name = 'memes_detail.html'


class TagsCloudView(generic.ListView):
    model = Tags
    context_object_name = 'tags_list'
    template_name = 'tags_list.html'







def normalize_query(query_string):
    string = query_string.replace(" ", '')
    string = string.replace('"', '')
    string = string.split(',')
    return string


class SearchResultsView(generic.ListView):
    model = Memes
    template_name = 'search_results.html'
    context_object_name = 'search_results'
    paginate_by = 20
    


    def get_queryset(self):
        query_string = ''
        object_list = None

        search_type = self.request.GET.get('search_type')
         
        if search_type == 'tag' and 'q' in self.request.GET:
            #   Bad but working way
            query_string = self.request.GET['q']
            search_tags = normalize_query(query_string)
            object_list = Memes.objects.filter(**{'tags__name': search_tags[0]})
            for tag in search_tags[1:]:
                object_list = object_list.filter(**{'tags__name': tag})

        elif search_type == 'title' and 'q' in self.request.GET:
            query_string = self.request.GET.get('q')
            object_list = Memes.objects.filter(Q(name__icontains=query_string))

        else:
            object_list = Memes.objects.all()

        return object_list



    def get_context_data(self, **kwargs):
        list_search = self.get_queryset()
        paginator = Paginator(list_search, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context = {
            'search_results': posts,
            'posts': posts
        }

        return context


class RandomMemesView(generic.DetailView):
    model = Memes
    template_name = 'random_memes_detail.html'

    def get_object(self):
        id_set = Memes.objects.values_list('id', flat=True)
        pk = random.choice(id_set)
        return Memes.objects.get(pk=pk)

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
    paginate_by = 1

class MemesDetailView(generic.DetailView):
    model = Memes
    template_name = 'memes_detail.html'

class TagsCloudView(generic.ListView):
    model = Tags 
    context_object_name = 'tags_list'
    template_name = 'tags_list.html'


def normalize_query(query_string,
    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
    normspace=re.compile(r'\s{2,}').sub):


    return [normspace('',(t[0] or t[1]).strip()) for t in findterms(query_string)]


class SearchResultsView(generic.ListView):
    model = Memes
    template_name = 'search_results.html'
    context_object_name = 'search_results'   
    paginate_by = 2

#    def get_queryset(self): 
#        query = self.request.GET.get('q')
#        object_list = Memes.objects.filter(
#            Q(tags__name__iexact=query)
#        )
#        return object_list

#    def normalize_query(query_string,
#        findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
#        normspace=re.compile(r'\s{2,}').sub):
#
#
#        return [normspace('',(t[0] or t[1]).strip()) for t in findterms(query_string)]

    def get_query(self, query_string, search_fields):


        query = None ## Query to search for every search term
        terms = self.normalize_query(query_string)
        for term in terms:
            or_query = None ## Query to search for a given term in each field
            for field_name in search_fields:
                q = Q(**{"%s__iexact" % field_name: term})
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query & or_query

    def get_queryset(self):
        query_string = ''
        object_list = None
        if ('q' in self.request.GET) and self.request.GET['q'].strip():
           query_string = self.request.GET['q']
           entry_query = self.get_query(query_string, ['tags__name'])
           object_list = Memes.objects.filter(entry_query)

        return object_list

	
    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
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
     template_name = 'memes_detail.html'
     def get_object(self):
         max_id = Memes.objects.all().aggregate(max_id=Max("id"))['max_id']
         pk = random.randint(1, max_id)
         return Memes.objects.get(pk=pk)



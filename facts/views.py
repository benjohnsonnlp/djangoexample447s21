from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from facts.models import CatFact


def index(request):
    facts = CatFact.objects.filter()
    context = {
        'facts': facts,
    }
    return render(request, 'facts/index.html', context=context)


def add(request):
    fact_text = request.POST['fact']
    image_url = request.POST['image_url']
    fact = CatFact(text=fact_text, image_url=image_url)
    fact.save()
    return HttpResponseRedirect(reverse('index'))

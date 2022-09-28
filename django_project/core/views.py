import datetime
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import TemplateView
import requests
import json


# Create your views here.

def displayTime(request):
    now = datetime.datetime.now()
    text = "The time is {}".format(now)
    return HttpResponse(text)

class testView(View):
    def get(self, request):
        return HttpResponse("Test view")

# class IndexView(TemplateView):
#     template_name = 'index.html'

def pokemon_detail(request):
    #response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=100').json()
    #results = response['results']
    list = [{
        'name': 'person', 
        'surname':'hello', 
        'dob':'something',
        'name': 'john',
    }]
    # for l in range(0, 101):
    #     image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png".format(l)
    #     #print(image_url)
    #     empty_list.append({
    #         'image_url': image_url,
    #     })
    # for i in results:
    #     digits = [d for d in i['url'] if d.isdigit()]
    #     digit = ''.join(digits)
    
    return render(request, "index.html", {"response": list})

def berry(request):
    response = requests.get('https://pokeapi.co/api/v2/berry/?limit=100').json()
    results = response['results']
    
    return render(request, "berry.html", {"response": results,})
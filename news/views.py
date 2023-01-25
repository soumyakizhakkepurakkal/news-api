from django.shortcuts import render
import requests

def index(request):
    response = requests.get('https://inshorts.deta.dev/news?category=science')
    posts = response.json()
    data = posts['data']
    return render(request,'index.html',{'data':data})

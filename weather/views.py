from django.shortcuts import render,redirect
from weather.models import City
import requests
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):

    if request.method=='POST':
        city=request.POST.get('city')
        contest=City(name=city)
        data = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=470551ef1a3184b421bb48e0a32b67d6'.format(city))
        if data:
            contest.save()
        else:
            messages.success(request, 'The city name you have entered is not in the database please check spelling')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=470551ef1a3184b421bb48e0a32b67d6'



    cities = City.objects.all()

    weather_data = []

    for city in cities :
        data = requests.get(url.format(city.name)).json()
        sunr =data['sys']['sunrise']
        sunrise = datetime.fromtimestamp(sunr)
        suns =data['sys']['sunset']
        sunset = datetime.fromtimestamp(suns)

        weather = {
            'city' : city.name,
            'id' : city.id,
            'temperature' :data['main']['temp'],
            'description' :data['weather'][0]['description'],
            'icon' :data['weather'][0]['icon'],
            'humidity' :data['main']["humidity"],
            'pressure' :data['main']["pressure"],
            'winds' :data['wind']["speed"],
            'windd' :data['wind']["deg"],
            'visibility' :data['visibility'],
            'clouds' :data['clouds']['all'],
            'country' :data['sys']['country'],
            'low' :data['main']["temp_min"],
            'high' :data['main']["temp_max"],
            'feel' :data['main']["feels_like"],
            'sunrise' : sunrise,
            'sunset' : sunset,
            'unit' : 'C'

        }

        weather_data.append(weather)



    context = {'weather_data' : weather_data}
    return render(request,'index.html',context)

def imperial(request):

    if request.method=='POST':
        city=request.POST.get('city')
        contest=City(name=city)
        data = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=470551ef1a3184b421bb48e0a32b67d6'.format(city))
        if data :
            contest.save()
        else:
            messages.success(request, 'The city name you have entered is not in the database please check spelling')

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=470551ef1a3184b421bb48e0a32b67d6'



    cities = City.objects.all()

    weather_data = []

    for city in cities :
        data = requests.get(url.format(city.name)).json()
        sunr =data['sys']['sunrise']
        sunrise = datetime.fromtimestamp(sunr)
        suns =data['sys']['sunset']
        sunset = datetime.fromtimestamp(suns)

        weather = {
            'city' : city.name,
            'id' : city.id,
            'temperature' :data['main']['temp'],
            'description' :data['weather'][0]['description'],
            'icon' :data['weather'][0]['icon'],
            'humidity' :data['main']["humidity"],
            'pressure' :data['main']["pressure"],
            'winds' :data['wind']["speed"],
            'windd' :data['wind']["deg"],
            'visibility' :data['visibility'],
            'clouds' :data['clouds']['all'],
            'country' :data['sys']['country'],
            'low' :data['main']["temp_min"],
            'high' :data['main']["temp_max"],
            'feel' :data['main']["feels_like"],
            'sunrise' : sunrise,
            'sunset' : sunset,
            'unit' : 'F'

        }

        weather_data.append(weather)



    context = {'weather_data' : weather_data}
    return render(request,'imperial.html',context)

def delete(request,n):
    City.objects.filter(id=n).delete()
    return redirect('/')

import json  
from django.shortcuts import render  
import urllib.request  
import json  
  
# Create your views here.  
  
def home(request):  
    if request.method == 'POST':  
        city = request.POST.get('city') or "Delhi"
          
        # retreive the information using api  
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=b943391a73c916380906753321ba1e31').read()  
          
        # convert json data file into python dictionary  
        list_of_data = json.loads(source)  
  
        # create dictionary and convert value in string  
        context = {  
            'city': str.capitalize(city),  
            "country_code": str(list_of_data['sys']['country']),  
            "coordinate": str(list_of_data['coord']['lon']) + ' '  
                            + str(list_of_data['coord']['lat']),  
            "temp": str(list_of_data['main']['temp']) + '°C',  
            "feels_like": str(list_of_data['main']['feels_like']) + '°C',
            "temp_min": str(list_of_data['main']['temp_min']) + '°C',
            "temp_max": str(list_of_data['main']['temp_max']) + '°C',
            "pressure": str(list_of_data['main']['pressure']),  
            "humidity": str(list_of_data['main']['humidity']),  
            "description": str.capitalize(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
            "wind": str(list_of_data['wind']['speed']) + ' meter/sec',
            "visibility": str(list_of_data['visibility']),
        }  
    else:  
        context = {}  
    return render(request, 'index.html', context)
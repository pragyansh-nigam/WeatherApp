from django.shortcuts import render

# Create your views here.

import json
# urllib.request to make a request to api
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid="your api_key here "  '''

        # source contain json data from api

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53').read()

        # converting json data to dictionary

        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lat']) + '° N, ' + str(list_of_data['coord']['lon']) + '° E',
            "temp": str(list_of_data['main']['temp']) + 'K',
            "pressure": str(list_of_data['main']['pressure']) + ' mb',
            "humidity": str(list_of_data['main']['humidity']) + '%'
        }
        print(data)
    else:
        data={}
    return render(request, "index.html", data)
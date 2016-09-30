import requests
import json

last_fm_api_key  = 'fa15d1b3850fd471297957941d4839f4'

artist = raw_input()
callback_url = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=' + artist +'&api_key='+last_fm_api_key+'&limit=10&format=json'
i=0
r = requests.get(callback_url)
data = json.loads(r.text)
#print data
for i in range(0,10):
    print data['toptracks']['track'][i]['name']
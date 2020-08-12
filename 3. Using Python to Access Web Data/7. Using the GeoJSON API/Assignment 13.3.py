import urllib.request
import urllib.parse
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"

address = input("Enter location: ")

params = {"sensor": "false", "address": address}
url = serviceurl + urllib.parse.urlencode(params)

print(f"Retrieving {url}")

data = urllib.request.urlopen(url).read().decode('utf-8')
print(f"Retrieved {len(data)} characters")
json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print("Place id", place_id)

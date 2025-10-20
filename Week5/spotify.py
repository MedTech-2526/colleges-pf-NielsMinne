import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Gebruik: python songs.py <zoekterm>")

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=10&term={sys.argv[1]}")

# Print de ruwe JSON-data
print(json.dumps(response.json(), indent=2))

# Toon alleen de tracknaam
o = response.json()
for result in o['results']:
    print("Tracknaam:", result['trackName'])
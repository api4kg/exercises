import requests

endpoint_url = "https://query.wikidata.org/sparql"
query_string = "SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q5741069.  SERVICE wikibase:label { bd:serviceParam wikibase:language \"[AUTO_LANGUAGE],en\". }}"

params = {'query' : query_string}
headers = {'accept' : 'application/json'}
r = requests.get(endpoint_url, params=params, headers=headers)

print(r.text)

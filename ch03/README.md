# Web data APIs over SPARQL

1. Example of the metadata and server routes sections of an OpenAPI specification - [YAML](./example1.yaml)

```yaml
openapi: 3.0.0
info:
  title: Music Bands API
  description: Provides information about music bands. This description supports [CommonMark](http://commonmark.org/) or HTML syntax.
  version: 1.2.1
servers:
  - url: http://api.rockbands.io/v1
    description: Main (production) server  # This description is optional
  - url: http://staging-api.rockbands.io
    description: Internal staging server for testing # This description is optional
```

2. Example of the paths section of an OpenAPI specification - [YAML](./example2.yaml)

```yaml
paths:
  /bands/{band_id}:
    description: Returns a band by its id, and optionally its location details
    parameters:
    - name: band_id
      in: path
      required: true
      description: the band identifier
      schema:
        type: integer
    - name: includeLocation
      in: query
      description: whether to return the band's location
      required: false
      schema:
        type: boolean
    get:
      responses:
        '200':
          description: the band being returned
          content:
            application/json:
              schema:
                type: object
                properties:
                  id: # the unique band id
                    type: integer
                  name: # the band's name
                    type: string
                    format: binary
                  location: # the band's location
                    type: string
                    format: binary
```

3. Example of the implementation of an API path in Python, as defined in an excerpt of an OpenAPI specification - [Python script](./example3.py)

```python
@app.route('/bands/{band_id}', method = ['GET'])
def band(band_id):
    """Returns a band by its id, and optionally its location details"""

    includeLocation = request.args['includeLocation'] # Capture the optional query parameter
    result = db.select('bands', band_id, includeLocation)

    ... # Some result post-processing as needed

    response = {'id': result.id, 'name': result.name , 'location' : result.location }

    return jsonify(response)
```

4. Query that retrieves all rock bands in Wikidata - [SPARQL](./example4.rq)

```sparql
SELECT ?item ?itemLabel ?locationLabel
WHERE {
    ?item wdt:P31 wd:Q5741069 .
    ?item wdt:P740 ?location .
    SERVICE wikibase:label {
      bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en"
    }
}
```

5. Example of the implementation of an API path in Python, querying the Wikidata SPARQL endpoint instead of a local database - [Python script](./example5.py)

```python
@app.route('/bands/{band_id}', method = ['GET'])
def band(band_id):
    """Returns a band by its id, and optionally its location details"""

    # Capture the optional query parameter
    includeLocation = request.args['includeLocation']

    endpoint_url = "https://query.wikidata.org/sparql"
    query_string = """
    SELECT ?item ?itemLabel ?locationLabel
        WHERE {
            ?item wdt:P31 wd:Q5741069 .
            ?item wdt:P740 ?location .
            VALUES ?item (___id___)
            SERVICE wikibase:label { bd:serviceParam
                    wikibase:language "[AUTO_LANGUAGE],en" }
        }"""
    query_string.replace("___id___", id)

    # Prepare HTTP request
    payload = {'query' : query_string}
    headers = {'accept' : 'application/json'}
    r = requests.get(endpoint_url, params=payload, headers=headers)

    data = r.json()
    response = {'id': data['item'], 'name': data['itemLabel']}
    if includeLocation:
        response['location'] = data['locationLabel']

    return jsonify(response)
```

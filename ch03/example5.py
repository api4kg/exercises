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

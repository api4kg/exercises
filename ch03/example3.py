@app.route('/bands/{band_id}', method = ['GET'])
def band(band_id):
    """Returns a band by its id, and optionally its location details"""
    includeLocation = request.args['includeLocation'] # Capture the optional query parameter
    result = db.select('bands', band_id, includeLocation)

    # Some result post-processing as needed

    response = {'id': result.id, 'name': result.name , 'location' : result.location }

    return jsonify(response)

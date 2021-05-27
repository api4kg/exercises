// Define the DBO namespace
var DBO = Namespace("http://dbpedia.org/ontology/");
var RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#");

// The store is the object that contains all triples
var store = $rdf.graph();

var band = $rdf.sym('http://dbpedia.org/resource/AC/DC');

// Insert triples in the store
store.add(band, RDFS('label'), 'AC/DC');
store.add(band, DBO('genre'), $rdf.sym('http://dbpedia.org/resource/Hard_rock'));
store.add(band, DBO('genre'), $rdf.sym("http://dbpedia.org/resource/Rock_and_roll"));

// Retrieve all (each) or one (any) results, using wildcards
var genres = store.each(band, DBO('genre'), undefined)
for (var genre of genres)
  console.log(genre.uri);

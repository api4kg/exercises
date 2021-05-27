# Chapter 2 - Accessing Knowledge Graphs programmatically

- [HTTP requests](#HTTP-Requests)
- [SPARQL Libraries](#SPARQL-Libraries) : SPARQL Wrapper, RDFLib, Jena
- [Manipulating output from SPARQL](#Manipulating-output-from-SPARQL) : rdflib.js, LDFlex, GraphQL-LD HyperGraphQL

## HTTP Requests

1. SPARQL query to retrieve all rock groups, and their English labels, from Wikidata. - [SPARQL](./example1.rq)

```sparql
SELECT ?item ?itemLabel
WHERE {
  ?item wdt:P31 wd:Q5741069.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```
2. HTTP request retrieving rock groups from the Wikidata SPARQL endpoint service - [direct link](https://query.wikidata.org/sparql?query=SELECT%20%3Fitem%20%3FitemLabel%20%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20wdt%3AP31%20wd%3AQ5741069.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D)

```
GET https://query.wikidata.org/sparql?query=SELECT%20%3Fitem%20%3FitemLabel%20%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20wdt%3AP31%20wd%3AQ5741069.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D
```

3. Using `curl` to transfer HTTP data about rock groups from the Wikidata SPARQL endpoint. We set the HTTP header `Accept` to ask the endpoint to send back the response in JSON format. - [bash file](./example3.sh)

```
curl -H'Accept: application/json' -X GET "https://query.wikidata.org/sparql?query=SELECT%20%3Fitem%20%3FitemLabel%20%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20wdt%3AP31%20wd%3AQ5741069.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D"
```

4. Send a SPARQL query to Wikidata via HTTP using the Python library `requests`. - [Python Script](./example4.py)

```python
import requests

endpoint_url = "https://query.wikidata.org/sparql"
query_string = "SELECT ?item ?itemLabel WHERE { ?item wdt:P31 wd:Q5741069.  SERVICE wikibase:label { bd:serviceParam wikibase:language \"[AUTO_LANGUAGE],en\". }}"

params = {'query' : query_string}
headers = {'accept' : 'application/json'}
r = requests.get(endpoint_url, params=params, headers=headers)

print(r.text)
```

## SPARQL Libraries

5. Sending a SPARQL query to an endpoint with [SPARQL Wrapper](https://github.com/RDFLib/sparqlwrapper) - [Python script](./example5.py)

```python
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE {
        <http://dbpedia.org/resource/Barcelona> rdfs:label ?label
    } """)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["label"]["value"])
```


6. Retrieving file-like RDF data (local or remote) and querying it with SPARQL and [RDFLib](https://github.com/RDFLib/rdflib) - [Python script](./example6.py)

```python
import rdflib

g = rdflib.Graph()
g.parse("http://example.org/rdf-data.nt")

qres = g.query(
    """
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?bandname
    WHERE {
          ?a rdf:type dbo:Band ;
             rdfs:label ?bandname .
    } """)

for row in qres:
    print(row)
```

7. Retrieving file-like RDF data (local or remote) and querying it using RDFLib iterators - [Python script](./example7.py)

```python
import rdflib
from rdflib import URIRef
from rdflib.namespace import RDF, RDFS

g = rdflib.Graph()
g.parse("http://example.org/rdf-data.nt")

for s,p,o in g.triples((None, RDF.type, URIRef("http://dbpedia.org/ontology/Band"):
    for u,v,s in g.triples((s, RDFS.label, None)):
        print(s)
```

8. Sending a SPARQL query to an endpoint with Jena - [Java class](./example8.java)

```java
import org.apache.jena.query.*;

public class JenaTest {
    public static void main(String []args) {
        String endpoint = "http://dbpedia.org/sparql";
        String queryString =
           "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n" +
           "SELECT ?label \n" +
           "WHERE {  \n" +
           "<http://dbpedia.org/resource/Barcelona> rdfs:label ?label"
           + "\n }";

        Query query = QueryFactory.create(queryString);
        QueryExecution qexec = QueryExecutionFactory.sparqlService(endpoint, query);
        try {
            ResultSet results = qexec.execSelect();
            ResultSetFormatter.out( results );
        }
        finally {
            qexec.close();
        }
    }
}
```

## Manipulating output from SPARQL

8. Creating and manipulating RDF data in [rdflib.js](https://github.com/linkeddata/rdflib.js/) - [JS script](./example9.js)

```js
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
```

10. Manipulating RDF data in [LDFlex](https://github.com/LDflex/LDflex) - [JS script](./example10.js)

```js
const { PathFactory } = require('ldflex');
const { default: ComunicaEngine } = require('@ldflex/comunica');
const { namedNode } = require('@rdfjs/data-model');

// The context maps properties and URIs
const context = {
  "@context": {
    "@vocab": "http://dbpedia.org/ontology/",
    "label": "http://www.w3.org/2000/01/rdf-schema#label",
  }
};

// The query engine interact with the SPARQL endpoint
const endpoint = 'http://dbpedia.org/sparql';
const queryEngine = new ComunicaEngine(endpoint);

// The PathFactory is the access point to the data
const path = new PathFactory({ context, queryEngine });

// define the band node as subject for queries
const band = path.create({
  subject: namedNode('http://dbpedia.org/resource/AC/DC')
});
getGenres(band);

async function getGenres(band) {
  // Under the hood, SPARQL queries are executed
  console.log(`This band is ${await band.label}`);

  console.log(`${await band.label} usually plays:`);
  for await (const genre of band.genre.label)
    console.log(`- ${genre}`);
}
```

11. A [query](./example11.gql) in [GraphQL-LD](https://comunica.github.io/Article-ISWC2018-Demo-GraphQlLD/), with its related context in [JSON-LD](./example11.json).

```gql
{
  label @single
  album {
    label
  }
  genre(label_en: "Hard rock")  @single
}
```

```json
{
  "@context": {
    "label": "http://www.w3.org/2000/01/rdf-schema#label",
    "label_en": { "@id": "http://www.w3.org/2000/01/rdf-schema#label", "@language": "en" },
    "album": { "@reverse": "http://dbpedia.org/ontology/album" },
    "genre": "http://dbpedia.org/ontology/genre"
  }
}
```

12. [Configuration](./example12.json), [schema](./example12_schema.gql) and [query](./example12.gql) in [HyperGraphQL](https://www.hypergraphql.org/)

```json
{
    "name": "my-api",
    "schema": "schema.graphql",
    "server": {
       "port": 8080,
       "graphql": "/graphql",
       "graphiql": "/graphiql"
    },
    "services": [{
       "id": "dbpedia-sparql",
       "type": "SPARQLEndpointService",
       "url": "http://dbpedia.org/sparql/",
       "graph": "http://dbpedia.org",
       "user": "",  "password": ""
    }]
}
```

```gql
type __Context {
    Band:  _@href(iri: "http://dbpedia.org/ontology/Band")
    Genre: _@href(iri: "http://dbpedia.org/ontology/Genre")
    label: _@href(iri: "http://www.w3.org/2000/01/rdf-schema#label")
    genre: _@href(iri: "http://dbpedia.org/ontology/genre")
}
type Band @service(id:"dbpedia-sparql") {
    label: [String] @service(id:"dbpedia-sparql")
    genre: Genre @service(id:"dbpedia-sparql")
}
type Genre @service(id:"dbpedia-sparql") {
    label: [String] @service(id:"dbpedia-sparql")
}
```

```gql
{
  Band_GET(limit: 1) {
    _id
    _type
    label
    genre {
      _id
      label(lang: "en")
    }
  }
}
```

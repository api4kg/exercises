# Chapter 1 - Introduction

## Examples

1. Some RDF statements (triples) serialised as[ N-Triples](./example1.nt)

```nt
<http://dbpedia.org/resource/AC/DC> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Band> .
<http://dbpedia.org/resource/AC/DC> <http://dbpedia.org/ontology/genre> <http://dbpedia.org/resource/Hard_rock> .
<http://dbpedia.org/resource/AC/DC> <http://dbpedia.org/ontology/genre> <http://dbpedia.org/resource/Blues_rock> .
<http://dbpedia.org/resource/AC/DC> <http://dbpedia.org/ontology/activeYearsStartYear> "1973"^^<http://www.w3.org/2001/XMLSchema#gYear> .
```

2. Some RDF statements (triples) serialised as [Turtle](./example2.ttl)

```ttl
@prefix dbr: <http://dbpedia.org/resource/> .
@prefix dbo: <http://dbpedia.org/ontology/Band> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

dbr:AC/DC a dbo:Band ;
          dbo:genre dbr:Hard_rock, dbr:Blues_rock ;
          dbo:activeYearsStartYear "1973"^^xsd:gYear .
```

3. Some RDF statements with named graphs (quads) serialised as [N-Quads](./example3.nq)

```nq
<http://dbpedia.org/resource/AC/DC> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Band> <http://bands.org/awesome-bands> .
<http://dbpedia.org/resource/AC/DC> <http://dbpedia.org/ontology/genre> <http://dbpedia.org/resource/Hard_rock> <http://bands.org/awesome-bands> .
<http://dbpedia.org/resource/AC/DC> <http://dbpedia.org/ontology/genre> <http://dbpedia.org/resource/Blues_rock> <http://bands.org/awesome-bands> .
<http://dbpedia.org/resource/AC/DC> <http://dbpedia.org/ontology/activeYearsStartYear> "1973"^^<http://www.w3.org/2001/XMLSchema#gYear> <http://bands.org/awesome-bands> .
```

4. Some RDF data, serialised as [JSON-LD](./example4.json)

```json
{
  "@context": "http://dbpedia.org/ontology/",
  "@graph": {
    "@id": "http://dbpedia.org/resource/AC/DC",
    "@type": "http://dbpedia.org/ontology/Band",
    "genre": [
      "http://dbpedia.org/resource/Hard_rock",
      "http://dbpedia.org/resource/Blues_rock"
    ],
    "activeYearsStartYear": {
      "@value": "1973",
      "@type":
        "http://www.w3.org/2001/XMLSchema#gYear"
    }
  }
}
```

5. Minimal example of a SPARQL [SELECT query](./example5.rq)

```sparql
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?band WHERE {
  ?band rdf:type dbo:Band .
} LIMIT 100
```

6. Example of GraphQL [query](./example6.graphql) and a possible [result object](./example6.json)

```graphql
{
  band: {
      name
      genre
      founded_in
  }
}
```

```json
{
  "band": {
      "name": "AC/DC",
      "genre": "Hard Rock",
      "founded_in": 1973
  }
}
```

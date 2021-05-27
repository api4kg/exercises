# Chapter 5 - Shaping JSON results: SPARQL Transformer

- [Examples]('#Examples')
- [Exercises]('#Exercises')

## Examples

1.  An example of JSON Query, in which it is possible to distinguish the prototype definition and the $-modifiers. - [JSON](./example1.json)

```json
{
  "proto": {
    "id"    : "?band",
    "album" : "?album",
    "genre" : "$dbo:genre$required"
  },
  "$where" : [
    "?band a dbo:Band",
    "?album a schema:MusicAlbum",
    "?album dbo:artist ?band"
  ],
  "$limit": 100
}
```

2.  A JSON query for retrieving the list of music bands, with labels, albums and genres - [JSON](./example2.json)

```json
{
  "proto" : {
    "id"    : "?band",
    "name"  : "$rdfs:label$required",
    "album" : "?album",
    "genre" : {
    	  "id"   : "$dbo:genre$required",
	      "label": "$rdfs:label$required"
    }
  },
  "$where": [
        "?band a dbo:Band",
        "?album a schema:MusicAlbum",
        "?album dbo:artist ?band"
  ],
  "$limit": 100
}
```

The equivalent SPARQL Query: [SPARQL](./example2.rq)

```sparql
SELECT DISTINCT ?band ?album ?v1 ?v2 ?v3
WHERE {

?band rdfs:label ?v1 .


?band dbo:genre ?v2 .
?v2 rdfs:label ?v3 .


?band a dbo:Band .
?album a schema:MusicAlbum .
?album dbo:artist ?band.
}
LIMIT 100
```

3.  Another example of a JSON query - [JSON](./example3.json)

```json
{
  "proto" : {
    "id"     : "?work",
    "name"   : "$rdfs:label$required$var:title",
    "image"  : "$foaf:depiction$sample",
    "museum" : "$dbo:museum$var:museum",
    "author" : {
      "uri"  : "$dbo:author$anchor$var:author",
      "name" : "$rdfs:label$lang$required",
      "worksCount" : "$dbo:author$reverse$count"
    }
  },
  "$where"    : "?work a dbo:Work",
  "$filter"   : "?author != dbr:Raphael",
  "$orderby"  : "desc(?title)",
  "$lang"     : "en;q=1, it;q=0.7 *;q=0.1",
  "$limit"    : 100,
  "$values"   : { "museum": "dbr:Louvre" },
  "$prefixes" : {
       "dbr" : "http://dbpedia.org/resource/",
       "dbo" : "http://dbpedia.org/ontology/"
  },
  "$langTag"  : "hide"
}
```

The equivalent SPARQL Query [SPARQL](./example3.rq)

```sparql
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?work ?title
(SAMPLE(?v2) AS ?v2) ?museum ?author ?v41 (COUNT(?v42) AS ?v42)
WHERE {
    VALUES ?museum {dbr:Louvre}

    ?work a dbo:Work.
    ?work rdfs:label ?title.
    ?work foaf:depiction ?v2.
    ?work dbo:museum ?museum.
    OPTIONAL {
        ?work dbo:author ?author .
        ?author rdfs:label ?v41 .
        FILTER(lang(?v41) = 'en').
        ?v42 dbo:author ?author
    }

    FILTER(?author != dbr:Raphael)
  }
  ORDER BY desc(?title)
  LIMIT 100
```

4. Using SPARQL Transformer in grlc with the `trasform` decorator [SPARQL](./example4.rq)


```sparql
#+ summary: Sample query for testing response transformation
#+ endpoint: "http://test-endpoint/transform/sparql/"
#+ transform: {
#+     "key": "?p",
#+     "value": "?o",
#+     "$anchor": "key"
#+   }

select ?p ?o where {
  ?_id_iri ?p ?o
} LIMIT 5
```

## Exercises

For solving the exercises, it is possible to use the [SPARQL Transformer Playground](https://d2klab.github.io/sparql-transformer/)), a web application for writing and testing JSON queries.

1. For each NBA player, retrieve his URI identifer, name, a single image (if available) and his birth date (if available). Solution: [JSON](./exercise1.json)
 - **_Tip_**: you may want to start by looking at [LeBron James](http://dbpedia.org/resource/LeBron_James) in DBpedia.

```json
{
  "proto": {
    "id": "?id",
    "name": "$rdfs:label$required",
    "league": "$dbo:league$var:league",
    "image": "$foaf:depiction$sample",
    "birthDate": "$dbo:birthDate"
  },
  "$values": {
    "league": "dbr:National_Basketball_Association"
  }
}
```

2. For each team in NBA (`?team dct:subject dbc:National_Basketball_Association_teams`),
retrieve the name of the team and the
the id and name for all players of the team.
For any name, be sure to pick the best label for an English-speaking public. Improve results readability by hiding the language tag. Solution: [JSON](./exercise2.json)

```json
{
  "proto": {
     "team" : "?team$anchor",
     "name": "$rdfs:label$required$bestlang",
     "players" : {
       "id": "$dbo:team$reverse",
       "name": "$rdfs:label$required$bestlang"
     }
  },
  "$where": "?team dct:subject dbc:National_Basketball_Association_teams",
  "$lang": "en",
  "$langTag": "hide"
}
```

3. For each country using the Euro as currency (`?country dbo:currency dbr:Euro`),
retrieve the id, the name, and the list of cities, together with city name and city population. Make sure to pick exactly the English labels and to hide the language tag. Limit the results to the first 100.  Solution:
[JSON](./exercise3.json)
 - **_Tip_**: you may start by looking at [Athens](http://dbpedia.org/resource/Athens) in DBpedia.

```json
{
  "proto": {
    "state": "?state$anchor",
    "name": "$rdfs:label$required$lang:en",
    "cities": {
        "id": "$dbo:country$reverse$var:city$required",
        "name": "$rdfs:label$required$lang:en",
        "population": "$dbo:populationTotal$required" }
  },
  "$where": [  "?state dbo:currency dbr:Euro",
      "?city a  dbo:City" ] ,
  "$langTag": "hide",
  "$limit" : 100
}
```

4. For each country using the Euro as currency,
retrieve the id, the name, and the total number of cities in the country. Order by descending number of cities. Make sure to pick exactly the English labels and to hide the language tag. Solution:
[JSON](./exercise4.json)

```json
{
  "proto": {
    "state": "?state$anchor",
    "name": "$rdfs:label$required$lang:en",
    "cities":  "$dbo:country$reverse$var:city$count"
  },
  "$where": [
      "?state dbo:currency dbr:Euro",
      "?city a dbo:City"
] ,
  "$orderby" : "desc(?city)",
  "$langTag": "hide"
}
```

5. Retrieve the list of Italian regions, with names and the list of cities in the region (id + label). Limit to the first 100 results and pick labels in Italian, hiding the language tag.
Use the JSON-LD syntax.
Make sure that your query is easily extensible to other countries and languages, for example France and French or United States and English. Solution:
[JSON](./exercise5.json)
  - **_Tip_**: you may start by looking at [Piedmont](http://dbpedia.org/resource/Piedmont) in DBpedia.

```json
{
  "@context": "http://example.org/",
  "@graph": [{
    "@type": "AdministrativeArea",
    "@id": "?id",
    "name": "$rdfs:label$required$lang",
    "country": "$dbo:country$required$var:country",
    "city": {
      "@id" : "$dbo:region$required$reverse$var:city",
      "name": "$rdfs:label$required$lang"
    }
  }],
  "$where": [
    "?id a dbo:AdministrativeRegion",
    "?city a dbo:City"
  ],
  "$values" : {
    "country" : "dbr:Italy"
  },
  "$lang": "it",
  "$langTag": "hide",
  "$limit": 100
}
```

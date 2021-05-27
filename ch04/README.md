# Chapter 4 - grlc: API automation by query sharing


### Examples

1. Querying list of band, album and genre from DBpedia - [SPARQL](./example1.rq)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX schema: <http://schema.org/>

SELECT ?band ?album ?genre WHERE {
  ?band rdf:type dbo:Band .
  ?album rdf:type schema:MusicAlbum .
  ?band dbo:genre ?genre .
  ?album dbo:artist ?band .
} LIMIT 100
```

2. Querying list of rock bands and albums from DBpedia - [SPARQL](./example2.rq)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX schema: <http://schema.org/>

SELECT ?band ?album WHERE {
  ?band rdf:type dbo:Band .
  ?album rdf:type schema:MusicAlbum .
  ?band dbo:genre <http://dbpedia.org/resource/Rock_music> .
  ?album dbo:artist ?band .
} LIMIT 100
```

3. Querying list of alternative bands and albums from DBpedia - [SPARQL](./example3.rq)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX schema: <http://schema.org/>

SELECT ?band ?album WHERE {
  ?band rdf:type dbo:Band .
  ?album rdf:type schema:MusicAlbum .
  ?band dbo:genre
            <http://dbpedia.org/resource/Alternative_rock> .
  ?album dbo:artist ?band .
} LIMIT 100
```

4. Querying list of bands and albums from DBpedia from a specified genre - [SPARQL](./example4.rq)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX schema: <http://schema.org/>

SELECT ?band ?album WHERE {
  ?band rdf:type dbo:Band .
  ?album rdf:type schema:MusicAlbum .
  ?band dbo:genre ?_genre_iri .
  ?album dbo:artist ?band .
} LIMIT 100
```


### Exercises
1. Create an API that retrieves all bands from DBpedia. Solution: [SPARQL](./exercise1.rq)

```sparql
#+ summary: Lists all DBpedia dbo:Band
#+ endpoint: http://dbpedia.org/sparql
#+ method: GET

PREFIX dbo: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?s
WHERE {
  ?s a dbo:Band
}
```


2. Create an API that lists bands that play either Rock or Jazz, and that have either Liverpool or Los Angeles as hometown. Solution: [SPARQL](./exercise2.rq)
  - **_Tip 1_**: Use the DBpedia ontology types `dbo:genre` and `dbo:hometown`.
  - **_Tip 2_**: Use the grlc `enumerate` decorator.

```sparql
#+ summary: Bands by city and genre
#+ endpoint: http://dbpedia.org/sparql
#+ tags:
#+   - dbpedia
#+ method: GET
#+ enumerate:
#+   - genre:
#+      - http://dbpedia.org/resource/Rock_music
#+      - http://dbpedia.org/resource/Jazz
#+   - hometown:
#+      - http://dbpedia.org/resource/Liverpool
#+      - http://dbpedia.org/resource/Los_Angeles

PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT DISTINCT ?s
WHERE {
  ?s a dbo:Band;
  dbo:genre ?_genre_iri;
  dbo:hometown ?_hometown_iri
}
```

3. Expand the API from the previous exercise by adding documentation and making sure your query can only be run on DBpedia SPARQL endpoint. Solution: [SPARQL](./exercise3.rq)
  - **_Tip_**: Use the `summary`, `description`, `endpoint` and `endpoint_in_url` decorators.

```sparql
#+ summary: Bands by city and genre
#+ description:
#+   This API endpoint lists bands from DBPedia that play either
#+   Rock or Jazz, and that have either Liverpool or Los Angeles as hometown.
#+ endpoint: http://dbpedia.org/sparql
#+ endpoint_in_url: false
#+ tags:
#+   - dbpedia
#+ method: GET
#+ enumerate:
#+   - genre:
#+      - http://dbpedia.org/resource/Rock_music
#+      - http://dbpedia.org/resource/Jazz
#+   - hometown:
#+      - http://dbpedia.org/resource/Liverpool
#+      - http://dbpedia.org/resource/Los_Angeles

PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT DISTINCT ?s
WHERE {
  ?s a dbo:Band;
  dbo:genre ?_genre_iri;
  dbo:hometown ?_hometown_iri
}
```


4. Create an API that lists the name, genre and hometown of bands whose name matches  a given  string. Solution: [SPARQL](./exercise4.rq)
  - **_Tip 1_**: Use the DBpedia property type `dbp:name`.
  - **_Tip 2_**: Because  DBpedia uses Virtuoso, you can use  the built in  function `bif:contains`.


```sparql
#+ summary: Bands by city and genre
#+ description:
#+   This API endpoint lists bands from DBPedia that play either
#+   Rock or Jazz, and that have either Liverpool or Los Angeles as hometown.
#+ endpoint: http://dbpedia.org/sparql
#+ endpoint_in_url: false
#+ tags:
#+   - dbpedia
#+ method: GET

PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
PREFIX bif: <bif:>

SELECT DISTINCT ?name ?genre ?hometown
WHERE {
?s a dbo:Band;
  dbp:name ?name;
  dbo:genre ?genre;
  dbo:hometown ?hometown .
  ?name bif:contains ?_bandname
} LIMIT 100
```

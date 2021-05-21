# Examples and Exercises

Examples and exercise for the book "​Web Data APIs for Knowledge Graphs"

## Chapter 4 - grlc: API automation by query sharing

Examples:
1. Querying list of band, album and genre from DBpedia - [SPARQL](./ch04/example1.rq)
1. Querying list of rock bands and albums from DBpedia - [SPARQL](./ch04/example2.rq)
1. Querying list of alternative bands and albums from DBpedia - [SPARQL](./ch04/example3.rq)
1. Querying list of bands and albums from DBpedia from a specied genre - [SPARQL](./ch04/example4.rq)

Exercises:
1. Create an API that retrieves all bands from DBpedia. Solution: [SPARQL](./ch04/exercise1.rq)
2. Create an API that lists bands that play either Rock or Jazz, and that have either Liverpool or Los Angeles as hometown. **_Tip 1_**: Use the DBpedia ontology types `dbo:genre` and `dbo:hometown`. **_Tip 2_**: Use the grlc `enumerate` decorator. Solution: [SPARQL](./ch04/exercise2.rq)
1. Expand the API from the previous exercise by adding documentation and making sure your query can only be run on DBpedia SPARQL endpoint.  **_Tip_**: Use the `summary`, `description`, `endpoint` and `endpoint_in_url` decorators. Solution: [SPARQL](./ch04/exercise3.rq)
1. Create an API that lists the name, genre and hometown of bands whose name matches  a given  string. **_Tip 1_**: Use the DBpedia property type `dbp:name`. **_Tip 2_**: Because  DBpedia uses Virtuoso, you can use  the built in  function `bif:contains`. Solution: [SPARQL](./ch04/exercise4.rq)

## Chapter 5 - Shaping JSON results: SPARQL Transformer

Examples:

1.  An example of JSON Query, in which it is possible to distinguish the prototype definition and the $-modifiers. - [JSON](./ch05/example1.json)
1.  A JSON query for retrieving the list of music bands, with labels, albums and genres - [JSON](./ch05/example2.json) - The equivalent SPARQL Query [SPARQL](./ch05/example2.rq)
1.  Another example of a JSON query - [JSON](./ch05/example3.json) - The equivalent SPARQL Query [SPARQL](./ch05/example3.rq)
1. Using SPARQL Transformer in grlc with the `trasform` decorator [SPARQL](./ch05/example4.rq)

Exercises (to be done in the [SPARQL Transformer Playground](https://d2klab.github.io/sparql-transformer/)):
1. For each NBA player, retrieve his URI identifer, name, a single image (if available) and his birth date (if available). **_Tip_**: you may want to start by looking at [LeBron James](http://dbpedia.org/resource/LeBron_James) in DBpedia. Solution: [JSON](./ch05/exercise1.json)
1. For each team in NBA (`?team dct:subject dbc:National_Basketball_Association_teams`),
retrieve the name of the team and the
the id and name for all players of the team.
For any name, be sure to pick the best label for an English-speaking public. Improve results readability by hiding the language tag. Solution: [JSON](./ch05/exercise2.json)
1. For each country using the Euro as currency (`?country dbo:currency dbr:Euro`),
retrieve the id, the name, and the list of cities, together with city name and city population. Make sure to pick exactly the English labels and to hide the language tag. Limit the results to the first 100. **_Tip_**: you may start by looking at [Athens](http://dbpedia.org/resource/Athens) in DBpedia. Solution:
[JSON](./ch05/exercise3.json)
1. For each country using the Euro as currency,
retrieve the id, the name, and the total number of cities in the country. Order by descending number of cities. Make sure to pick exactly the English labels and to hide the language tag. Solution:
[JSON](./ch05/exercise4.json)
1. Retrieve the list of Italian regions, with names and the list of cities in the region (id + label). Limit to the first 100 results and pick labels in Italian, hiding the language tag.
Use the JSON-LD syntax.
Make sure that your query is easily extensible to other countries and languages, for example France and French or United States and English.
Tip: you may start by looking at [Piedmont](http://dbpedia.org/resource/Piedmont) in DBpedia. Solution:
[JSON](./ch05/exercise5.json)

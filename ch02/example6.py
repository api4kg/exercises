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
    }""")

for row in qres:
    print(row)

import rdflib
from rdflib import URIRef
from rdflib.namespace import RDF, RDFS

g = rdflib.Graph()
g.parse("http://example.org/rdf-data.nt")

for s,p,o in g.triples((None, RDF.type, URIRef("http://dbpedia.org/ontology/Band"):
    for u,v,s in g.triples((s, RDFS.label, None)):
        print(s)

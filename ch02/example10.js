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

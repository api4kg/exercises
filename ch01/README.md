# Chapter 1 - Introduction

## Examples

1. JSON-LD containing some data about AC/DC - [JSON](./example1.json)

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

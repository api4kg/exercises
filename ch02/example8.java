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

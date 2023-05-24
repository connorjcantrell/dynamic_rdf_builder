from rdflib import Graph, exceptions

class DynamicRDFBuilder:
    """
    A class to dynamically build RDF Turtle files from ttx files.
    Placeholders in the ttx files are replaced with actual entity names.
    """

    def __init__(self, base_instance, base_ttx_file):
        """
        Initializes the RDFBuilder with a base entity name and a base ttx file.
        """
        self.base_instance = base_instance
        self.turtle_data = self.parse(base_ttx_file, [base_instance])

    def add(self, ttx_file, additional_instances):
        """
        Adds additional entities to the Turtle data from a ttx file.
        """
        additional_data = self.parse(ttx_file, [self.base_instance] + additional_instances)
        self.turtle_data += '\n' + additional_data

    def parse(self, ttx_file, instances):
        """
        Parses a ttx file, replaces placeholders with entity names, and returns Turtle data as a string.
        """
        with open(ttx_file, "r") as file:
            ttx_template = file.read()

        for index, instance in enumerate(instances):
            placeholder = "{" + str(index) + "}"
            if placeholder not in ttx_template:
                raise ValueError(f"Placeholder {placeholder} not found in ttx file.")
            ttx_template = ttx_template.replace(placeholder, instance)

        return ttx_template

    def build_graph(self):
        """
        Parses the Turtle data into an RDF graph, checking for validity.
        """
        rdf_graph = Graph()
        try:
            rdf_graph.parse(data=self.turtle_data, format='turtle')
        except exceptions.ParserError as e:
            raise ValueError("Invalid RDF data.") from e

        return rdf_graph

    def serialize(self, format='turtle'):
        """
        Serializes the RDF graph into a string in the given format.
        """
        rdf_graph = self.build_graph()
        return rdf_graph.serialize(format=format).encode('utf-8')

# DynamicRDFBuilder
This Python module allows users to construct RDF (Resource Description Framework) Turtle files dynamically. It takes a base `ttx` template file, which must contain the prefixes, and optionally additional ttx template files. It replaces placeholders in these template files with actual entity names to build a valid RDF Turtle file.

### What is a `ttx` file?
A ttx file is a Turtle (ttl) RDF template file with placeholders for entity names. These placeholders are written as {index}, where index is an integer starting from 0. For instance, a base ttx file might look something like this:
```ttl
@prefix ex: <http://example.org/> .
ex:{0} a ex:Entity .
```

and an additional `.ttx` file might look like this:
```
ex:{0} ex:hasRelation ex:{1} .
```

In the above examples, {0} and {1} are placeholders that will be replaced by actual entity names.

## Requirements
DynamicRDFBuilder requires `rdflib`

## Usage
```python
from dynamic_rdf_builder import DynamicRDFBuilder

# Instantiate the DynamicRDFBuilder with base entity name and base ttx file
rdf_builder = DynamicRDFBuilder('BaseEntity', 'thing.ttx')

# Add additional instances from another ttx file
rdf_builder.add('with_component.ttx', ['Entity2', 'Entity3'])

# Build the RDF graph (for checking validity)
rdf_graph = rdf_builder.build_graph()

# Serialize the RDF graph into a string (default format is 'turtle')
turtle_data = rdf_builder.serialize()
```

## Module Details
`DynamicRDFBuilder`
Main class in the module.

`__init__(self, base_instance, base_ttx_file)`
Constructor for the DynamicRDFBuilder class.
- base_instance: The name of the base entity.
- base_ttx_file: The path to the base ttx template file.

`add(self, ttx_file, additional_instances)`
Method to add additional entities from a ttx file.
- ttx_file: The path to the additional ttx template file.
     additional_instances: A list of additional entity names.

`parse(self, ttx_file, instances)`
Method to parse a ttx file, replace placeholders with entity names, and return Turtle data as a string.
- ttx_file: The path to the ttx template file.
- instances: A list of entity names.

`build_graph(self)`
Method to parse the Turtle data into an RDF graph, checking for validity.

`serialize(self, format='turtle')`
Method to serialize the RDF graph into a string in a specified format.
- format: The output format of the serialization (default is 'turtle').

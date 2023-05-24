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
rdf_builder.add('with_component.ttx', ['Component1'])

# Build the RDF graph (for checking validity)
rdf_graph = rdf_builder.build_graph()

# Serialize the RDF graph into a string (default format is 'turtle')
print(rdf_builder.serialize())
```

Output:
```
@prefix ex: <http://example.org/> .

ex:BaseEntity a ex:Entity ;
    ex:hasRelation ex:Component1 .
    ex:Component1 a ex:Component .
```

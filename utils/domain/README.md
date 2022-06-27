# Purpose:
The domain classes define ways to interact with a data source and an ontology in order to carry out a task-oriented dialog in a specific domain.

# Description of Files:
* `domain.py`: Defines a parent class for domains, creating a common interface for domain classes which should all have a domain name and a way to find entities
* `jsonlookupdomain.py`: Defines a domain class which takes in a JSON file as an ontology description and a SQLite database as a datasource
* `lookupdomain.py`: Defines a slighly more concrete interface for a domain object with method interfaces for reading an ontology

# Error that I encountered:
The following are the reasons for the ImportError: cannot import name

The import class is not available or not created.
The import class name is mis-named or mis-spelled
The import class name and module name is mis-placed.
The import class is not available in python class path
The import class is not available in python library
The import class is in circular dependency

link: https://www.yawintutor.com/importerror-cannot-import-name/

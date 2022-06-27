# Purpose:
The `nlg` folder contains code related to converting the semantic representation of a system action to a natural language representation (natural language generation). 

# File Descriptions:
* `templates`: A folder containing the logic for reading nlg template files and using them to convert `SysAct`s to natural language.
* `affective_nlg.py`: Defines a child of the `HandcraftedNLG` class which produces different natural language output depending on the emotion the system is tyring to output.
* `bc_nlg.py`: Defines a class which adds backchannels into the rule-based natural language output
* `nlg.py`: Defines a class which uses defined templates to convert system actions into natural language output.

# Modified for nlg folder
There are no `affective_nlg.py` and `bc_nlg.py` in this folder yet. If they are added in the folder, comment out the two imports in the `__init__.py`.

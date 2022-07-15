# Purpose:
This folder contains regex files, and templates for making regex files, which map natural language user input to user actions.

* `.nlu` files represent NLU templates which can be used to automatically generate regex files
* `.json` files represent the complete regexes used by the NLU
* three types of `.json` files:
  * **General**
     * Contain general (non-domain specific) regexes for English and German (based on end extension)
  * **InformRules**
    * Contain regexes for user informs
  * **RequestRules** 
    * Contain regexes for user requests
* File names are in the following formats:
  * For english files:
    * `{domain_name}{Type}{Language}.json`
    * If no language is specified, the file is in English

To build a new request rule with the requestable, which is not any column name in the database: 
    rule request(ingredient)
        "what do I need"
	
1. Add the requestable item, (e.g. ingredient) to ontology, `{domain name}.json`.

2. Add the rule to `{domain name}.nlu`. This is what user need to say to activate this request.

3. Execute the script `gen_regexes.py` in the folder `tools/regextemplates` like this:
`python3 tools/regextemplates/gen_regexes.py {domain_name} {domain_name}`.
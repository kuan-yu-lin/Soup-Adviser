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

# Not put them in soup.nlu yet:

rule inform(Ingredient)
    "I( only)? have {Ingredient}"
    "I( only)? have {Ingredient} and {Ingredient}"
    "I( only)? have {Ingredient}, {Ingredient} and {Ingredient}"
## will this work? the column name are the name of Ingredients.
## should we copy the rule and apply it to each Ingredient name?
## any better way to write this rule?

rule request(Ingredient)
    "what do I need to (make|do|prepare) {slot_synonyms("name")}"
    "waht are the {slot_synonyms("Ingredient")}"
    "do I need {slot_synonyms("Ingredient")} to (make|do|prepare) {slot_synonyms("name")}"
	
## we want it to return all Ingredients!!!

    
    add_if slot = "Ingredient"
        if value = "1"
            "one"
            
    if slot = "Ingredient"
        "ingredient(s)?"

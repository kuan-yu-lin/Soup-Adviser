# Question for soup.nlu:

## inform()
1. how to write the nlu rule for "I have 30 minutes", then I get all the recipes that the TotalTime of them are less than 30 minutes.

2. will the rule for ingredient work? the column name are the name of Ingredients. 
   should we copy the rule and apply it to each Ingredient name?
   is there a better way to present the following rule:
rule inform(Ingredient)
    "I( only)? have {Ingredient}"
    "I( only)? have {Ingredient} and {Ingredient}"
    "I( only)? have {Ingredient}, {Ingredient} and {Ingredient}"

## request()
3. "what do I do next" should this question be the rule for useract: 'repeat'?

4. should we set for getting 3 steps at one time? how?

5. we want it to return all Ingredients!!!

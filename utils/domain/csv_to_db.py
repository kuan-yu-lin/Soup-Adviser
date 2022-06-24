import pandas as pd
import sqlite3

# reference link: https://towardsdatascience.com/turn-your-excel-workbook-into-a-sqlite-database-bc6d4fd206aa

# Load CSV data into Pandas DataFrame
recipes = pd.read_csv('recipes.csv')
ingredients = pd.read_csv('ingredients.csv')
# print(df)

conn = sqlite3.connect('recipes.db') # Connect to SQLite database
cursor = conn.cursor() # Create a cursor object

# Fetch and display result 
# Recipes
cursor.execute(
    """
    CREATE TABLE Recipes(
        Name TEXT PRIMARY KEY,
        PrepTime INTEGER,
        CookingTime INTEGER,
        TotalTime INTEGER,
        Step1Prep TEXT,
        Step2Process TEXT,
        Step3Seasoning TEXT
        );
     """
)

# Fetch and display result
# Ingredients
cursor.execute(
    """
    CREATE TABLE Ingredients(
        Name TEXT,
        ChickenStock TEXT,
        ChickenBroth TEXT,
        CookedChicken TEXT,
        GroundBeef TEXT,
        Tofu TEXT,
        Eggs TEXT,
        Tomatoes TEXT,
        Potatoes TEXT,
        Carrots TEXT,
        Beans TEXT,
        Lentils TEXT,
        Corn TEXT,
        Broccoli TEXT,
        EvaporatedMilk TEXT,
        Cornstarch TEXT,
        JapaneseTurnip TEXT,
        Salsa TEXT,
        HotPepperSauce TEXT,
        Scallions TEXT,
        Onions TEXT,
        Leek TEXT,
        Celery TEXT,
        Cumin TEXT,
        Ginger TEXT,
        Thyme TEXT,
        Miso TEXT,
        Pasta TEXT,
        Garlic TEXT,
        Mushrooms TEXT,
        Basil TEXT,
        Kale TEXT,
        Avocado TEXT,
        PRIMARY KEY(Name),
        FOREIGN KEY(Name) REFERENCES Recipes(Name)
        );
    """
)

# Write the data to a sqlite table
recipes.to_sql('Recipes', conn, if_exists='append', index=False) 
ingredients.to_sql('Ingredients', conn, if_exists='append', index=False)

conn.close()

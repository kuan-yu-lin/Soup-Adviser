import pandas as pd
import sqlite3

# reference link: https://towardsdatascience.com/turn-your-excel-workbook-into-a-sqlite-database-bc6d4fd206aa

# Load CSV data into Pandas DataFrame
soup = pd.read_csv('/home/kuanyu/Documents/GitHub/Soup_Advisor/resources/databases/recipes.csv')
ingredient = pd.read_csv('/home/kuanyu/Documents/GitHub/Soup_Advisor/resources/databases/ingredients.csv')
# print(df)

conn = sqlite3.connect('soup.db') # Connect to SQLite database
cursor = conn.cursor() # Create a cursor object

cursor.execute(
    """
    DROP TABLE IF EXISTS soup;
    """
)

# Fetch and display result 
# recipe
cursor.execute(
    """
    CREATE TABLE soup(
        name TEXT PRIMARY KEY,
        prep_time INTEGER,
        cook_time INTEGER,
        total_time INTEGER,
        step_one TEXT,
        step_two TEXT,
        step_three TEXT
        );
    """
)

cursor.execute(
    """
    DROP TABLE IF EXISTS ingredient;
    """
)

# Fetch and display result
# ingredient
cursor.execute(
    """
    CREATE TABLE ingredient(
        name TEXT,
        chicken_stock TEXT,
        chicken_broth TEXT,
        cooked_chicken TEXT,
        ground_beef TEXT,
        tofu TEXT,
        egg TEXT,
        tomato TEXT,
        potato TEXT,
        carrot TEXT,
        bean TEXT,
        lentil TEXT,
        corn TEXT,
        broccoli TEXT,
        evaporated_milk TEXT,
        cornstarch TEXT,
        japanese_turnip TEXT,
        salsa TEXT,
        hot_pepper_sauce TEXT,
        scallion TEXT,
        onion TEXT,
        leek TEXT,
        celery TEXT,
        cumin TEXT,
        ginger TEXT,
        thyme TEXT,
        miso TEXT,
        pasta TEXT,
        garlic TEXT,
        mushroom TEXT,
        basil TEXT,
        kale TEXT,
        avocado TEXT,
        PRIMARY KEY(Name),
        FOREIGN KEY(Name) REFERENCES soup(Name)
        );
    """
)

# Write the data to a sqlite table
soup.to_sql('soup', conn, if_exists='append', index=False) 
ingredient.to_sql('ingredient', conn, if_exists='append', index=False)
# The .db file is sent to /home/

conn.close()

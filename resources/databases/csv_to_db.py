import pandas as pd
import sqlite3

# reference link: https://towardsdatascience.com/turn-your-excel-workbook-into-a-sqlite-database-bc6d4fd206aa

# Load CSV data into Pandas DataFrame
soup = pd.read_csv('/home/kuanyu/Documents/GitHub/soup_adviser/resources/databases/soup.csv')
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
        total_time INTEGER,
        step_one TEXT,
        step_two TEXT,
        step_three TEXT,
        chicken_stock INTEGER,
        chicken_broth INTEGER,
        cooked_chicken INTEGER,
        ground_beef INTEGER,
        tofu INTEGER,
        egg INTEGER,
        tomato INTEGER,
        potato INTEGER,
        carrot INTEGER,
        bean INTEGER,
        lentil INTEGER,
        corn INTEGER,
        broccoli INTEGER,
        evaporated_milk INTEGER,
        cornstarch INTEGER,
        japanese_turnip INTEGER,
        salsa INTEGER,
        hot_pepper_sauce INTEGER,
        scallion INTEGER,
        onion INTEGER,
        leek INTEGER,
        celery INTEGER,
        cumin INTEGER,
        ginger INTEGER,
        thyme INTEGER,
        miso INTEGER,
        pasta INTEGER,
        garlic INTEGER,
        mushroom INTEGER,
        basil INTEGER,
        kale INTEGER,
        avocado INTEGER
        );
    """
)

# Write the data to a sqlite table
soup.to_sql('soup', conn, if_exists='append', index=False) 

# The .db file is sent to /home/

conn.close()

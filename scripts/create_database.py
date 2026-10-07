import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv("data/superstore_cleaned.csv")

# Create SQLite database
connection = sqlite3.connect("data/superstore.db")

# Store dataframe as a table
df.to_sql("superstore", connection, if_exists="replace", index=False)

connection.close()

print("Database created successfully!")
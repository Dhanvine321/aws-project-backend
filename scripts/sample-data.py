import sqlite3
import json

def insert_data_from_json(file, table_name):
    """Inserts data from a JSON file into the specified table in the database."""

    conn = sqlite3.connect('./data/AWS.db')
    print("Opened database successfully\n")

    with open(file, 'r') as f:
        data = json.load(f)  # Load JSON data as a list of dictionaries

    with conn:
        cursor = conn.cursor()
        for row in data:
            values = tuple(row.values())  # Extract values from each dictionary
            cursor.execute("INSERT INTO {} VALUES ({})".format(table_name, ','.join('?' * len(values))), values)

    print("Data inserted successfully into table {}".format(table_name))

insert_data_from_json('./data/Jobs.json', 'Jobs')
insert_data_from_json('./data/Nurses.json', 'Nurses')

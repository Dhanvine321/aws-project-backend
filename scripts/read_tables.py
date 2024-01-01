
import sqlite3

def get_table_data(table_name):
    conn = sqlite3.connect('./data/AWS.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    columns = [col[0] for col in cursor.description]  # Get column names

    rows = cursor.fetchall()

    conn.close()

    # Convert each row to a dictionary using column names
    result = [dict(zip(columns, row)) for row in rows]

    #print(result)
    return result



# get_table_data('Jobs')
# get_table_data('Nurses')

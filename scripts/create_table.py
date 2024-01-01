import sqlite3
def create_tables():
    conn = sqlite3.connect('./data/AWS.db')
    print("Opened database successfully\n")
    with open("./scripts/table-create.sql", 'r') as f:
        sql = f.read()
    conn.executescript(sql)
    conn.close()
    print("Table created successfully\n")
    return None
create_tables()
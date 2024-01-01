import sqlite3

def delete_job(job_id):
    conn = sqlite3.connect('../data/AWS.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Jobs WHERE JobId = ?", (job_id,))

    conn.commit()
    conn.close()

def delete_nurse(nurse_id):
    conn = sqlite3.connect('../data/AWS.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Nurses WHERE NurseId = ?", (nurse_id,))

    conn.commit()
    conn.close()

# def delete_row(table_name, primary_keys):
#     conn = sqlite3.connect('../data/AWS.db')
#     cursor = conn.cursor()

#     # Build the WHERE clause dynamically based on the number of primary keys
#     where_clause = ' AND '.join(f'id{i+1} = ?' for i in range(len(primary_keys)))

#     cursor.execute(f"DELETE FROM {table_name} WHERE {where_clause}", primary_keys)

#     conn.commit()
#     conn.close()
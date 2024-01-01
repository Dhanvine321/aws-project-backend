import sqlite3

def add_data_to_table(table_name, data):
    conn = sqlite3.connect('./data/AWS.db')
    cursor = conn.cursor()

    columns = ', '.join(data.keys())
    placeholders = ', '.join(['?' for _ in data.values()])
    values = tuple(data.values())

    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(query, values)

    conn.commit()
    conn.close()

# Example usage

# data = {

#     "title": "Cardiac Nurse",
#     "description": "Cardiology Department",
#     "roleDescription": "Provide safe and quality nursing care for patients with heart conditions.",
#     "keyResponsibilities": "To assess, plan, implement and evaluate nursing care for cardiac patients.",
#     "requirements": "Minimum Diploma in Nursing or equivalent.\nCandidates with Advanced Diploma / Degree in Cardiac Nursing or equivalent.",
#     "applicants": "0",
#     "pay": "$25/hr",
#     "date": "09-01-2024",
#     "time": "8:30AM to 4:30PM"
# }

# add_data_to_table('Jobs', data)
# Import the flask module
import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS
import json     # To convert the dictionary to a JSON object
from flask_cors import cross_origin
from scripts.add_data import add_data_to_table
import scripts.read_tables as read_tables
import scripts.delete_data as delete_data
# Create a new Flask application
app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])
# A welcome message to test server
@app.route('/')
def index():
    return "<h1>Farrer Park Hosptial freelance website Backend Server</h1>"

# send nurses.json data to frontend 
@app.route('/nurses')   
def nurses():
     data = read_tables.get_table_data('Nurses')
    #  print(data)
    #  print(type(data))
    #  print(jsonify(data))
     return jsonify(data)

# send jobs.json data to frontend
@app.route('/jobs')
def jobs():
    data = read_tables.get_table_data('Jobs')
    # print(data)
    #  print(type(data))
    #  print(jsonify(data))
    return jsonify(data)

@app.route('/add_jobs', methods=['POST', 'OPTIONS'])
@cross_origin(origins=['http://localhost:3000'], methods=['POST', 'OPTIONS'], allow_headers=['Content-Type']) # Replace with your actual origin
def update_job():
    if request.method == 'OPTIONS':
        # Preflight request. Reply successfully:
        return '', 200
    # Get the data from the PUT request
    new_data = request.get_json()
    # print(new_data)
    # print(type(new_data))

    # Load the existing data
    add_data_to_table('Jobs', new_data)

    # Return a success message
    return jsonify({"message": "Data in Jobs.json updated successfully"}), 200




@app.route('/delete_jobs', methods=['DELETE', 'OPTIONS'])
@cross_origin() 
def delete_job():
    if request.method == 'OPTIONS':
        return '', 200
    # Get the key of the data to be deleted from the DELETE request
    job_id = request.get_json().get('JobId')
    # print(job_id)
    delete_data.delete_job(job_id)

    return jsonify({"message": f"Job with ID '{job_id}' deleted successfully"}), 200
if __name__ == '__main__':
    app.run()
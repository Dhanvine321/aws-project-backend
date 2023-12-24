# Import the flask module
from flask import Flask, jsonify, request
from flask_cors import CORS
import json     # To convert the dictionary to a JSON object
from flask_cors import cross_origin
# Create a new Flask application
application = Flask(__name__)
CORS(application, origins=['http://localhost:3000'])

# A welcome message to test server
@application.route('/')
def index():
    return "<h1>Farrer Park Hosptial freelance website Backend Server</h1>"

# send nurses.json data to frontend 
@application.route('/nurses')   
def nurses():
    with open('Nurses.json') as json_file:
        data = json.load(json_file)
        return jsonify(data) 
    
# update nurses.json data from frontend
@application.route('/add_nurses', methods=['PUT'])
def update_nurse():
    # Get the data from the PUT request
    new_data = request.get_json()

    # Load the existing data
    with open('nurses.json', 'r') as json_file:
        data = json.load(json_file)

    # Update the data with the new data
    data.update(new_data)

    # Write the updated data back to the file
    with open('nurses.json', 'w') as json_file:
        json.dump(data, json_file)

    # Return a success message
    return jsonify({"message": "Data in nurses.json updated successfully"}), 200

# delete nurses.json data from frontend
@application.route('/delete_nurses', methods=['DELETE', 'OPTIONS'])
def delete_nurse():
    if request.method == 'OPTIONS':
        # Preflight request. Reply successfully:
        return '', 200
    # Get the key of the data to be deleted from the DELETE request
    key_to_delete = request.get_json().get('key')

    # Load the existing data
    with open('nurses.json', 'r') as json_file:
        data = json.load(json_file)

    # Check if the key exists in the data
    if key_to_delete in data:
        # If it exists, delete it
        del data[key_to_delete]

        # Write the updated data back to the file
        with open('nurses.json', 'w') as json_file:
            json.dump(data, json_file)

        # Return a success message
        return jsonify({"message": f"Key '{key_to_delete}' deleted successfully"}), 200
    else:
        # If the key does not exist, return an error message
        return jsonify({"error": f"Key '{key_to_delete}' not found"}), 404

# send jobs.json data to frontend
@application.route('/jobs')
def jobs():
    with open('Jobs.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)

# update jobs.json data from frontend
@application.route('/add_jobs', methods=['POST', 'OPTIONS'])
@cross_origin(origins=['http://localhost:3000'], methods=['POST', 'OPTIONS'], allow_headers=['Content-Type']) # Replace with your actual origin
def update_job():
    if request.method == 'OPTIONS':
        # Preflight request. Reply successfully:
        return '', 200
    # Get the data from the PUT request
    new_data = request.get_json()
    print(new_data)
    # Load the existing data
    with open('Jobs.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)
    # Update the data with the new data
    data.append(new_data)

    # Write the updated data back to the file
    with open('Jobs.json', 'w') as json_file:
        json.dump(data, json_file)

    # Return a success message
    return jsonify({"message": "Data in Jobs.json updated successfully"}), 200

# delete jobs.json data from frontend
@application.route('/delete_jobs', methods=['DELETE', 'OPTIONS'])
@cross_origin() 
def delete_job():
    if request.method == 'OPTIONS':
        # Preflight request. Reply successfully:
        return '', 200
    # Get the key of the data to be deleted from the DELETE request
    print(request.get_json())
    key_to_delete = request.get_json().get('key')
    print(key_to_delete)
    # Load the existing data
    with open('Jobs.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)
        print(data[key_to_delete])
    # Check if the key exists in the data
    if key_to_delete < len(data):
        # If it exists, delete it
        
        del data[key_to_delete]

        # Write the updated data back to the file
        with open('Jobs.json', 'w') as json_file:
            json.dump(data, json_file)

        # Return a success message
        return jsonify({"message": f"Key '{key_to_delete}' deleted successfully"}), 200
    else:
        # If the key does not exist, return an error message
        return jsonify({"error": f"Key '{key_to_delete}' not found"}), 404
    
if __name__ == '__main__':
    application.run()
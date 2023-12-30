import json
import time
import threading
import time
from pprint import pprint
import random
import geocoder
from geopy.distance import geodesic

#set max sal and min sal
max_sal = 20
min_sal = 12
days_left = 10

def price_optimisation(max_sal, min_sal, days_left, applicants_count):
    # max_sal and min_sal are the max and min salary that the employer is willing to pay
    # days_left is the number of days left for the job deadline
    # applicants_count is the number of applicants applied for this job in a given period of time

    # calculate the days left factor
    days_left_factor = (30 - days_left) / 30

    # calculate the applicants count factor
    applicants_count_factor = max(0, (applicants_count - 1) / 100)

    # calculate the adjusted salary
    adjusted_sal = (1 - applicants_count_factor) * (min_sal + days_left_factor * (max_sal - min_sal))

    # ensure the adjusted salary is not less than the minimum salary
    adjusted_sal = max(adjusted_sal, min_sal)

    # return the adjusted salary
    return adjusted_sal

# test the price optimisation function
print(price_optimisation(18, 14, 7, 2))

# Function to create a dictionary with job names and pay
def create_jobs_dict():
    jobs_dict = {}

    # Read the Jobs.json file
    with open('Jobs.json', 'r') as file:
        jobs_data = json.load(file)

    # Iterate over each job and calculate the pay
    for job in jobs_data:
        job['applicants'] = random.randint(0, 20)
        job_name = job['title']
        job_pay = price_optimisation(max_sal, min_sal, 7, int(job['applicants']))
        job_pay = round(job_pay, 2)  # Round off to 2 decimal places
        jobs_dict[job_name] = [job_pay, job['applicants']]
    return jobs_dict

# Function to check and update the Jobs.json file
def check_and_update_jobs():
    while True:
        # Call the create_jobs_dict function
        jobs_dict = create_jobs_dict()

        # Print the dictionary
        print("------------------")
        pprint(jobs_dict)

        # Wait for 10 seconds
        time.sleep(10)

# Start updating the Jobs.json file in a separate thread
#update_jobs_thread = threading.Thread(target=check_and_update_jobs, args=())
#update_jobs_thread.start()


address1 = "Farrer Park Hospital, Singapore"
address2 = input("Enter the postalcode: ")
# make a function to use address and find the distance between two address
def distance(address1, address2):
    # Get the latitude and longitude of the first address
    g = geocoder.osm(address1, country="Singapore")
    latlng1 = g.latlng

    # Get the latitude and longitude of the second address
    g = geocoder.osm(address2, country="Singapore")
    latlng2 = g.latlng

    # Calculate the distance between the two coordinates
    dist = geodesic(latlng1, latlng2).km
    dist = round(dist, 2)  # Round off to 2 decimal places
    return '{dist} km'.format(dist=dist)

# test the distance function
print(distance(address1, address2))
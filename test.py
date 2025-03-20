import requests

# Define the API endpoint
url = 'http://127.0.0.1:5012/predict'

Account_Manager = 0 
Years = 2.0 
Num_Sites = 11 
Age = 30.0 

data = {
    'Age': Age,
    'Account_Manager': Account_Manager,
    'Years': Years,
    'Num_Sites': Num_Sites,
}

# Send a POST request
response = requests.post(url, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Print the prediction result
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.json()}")
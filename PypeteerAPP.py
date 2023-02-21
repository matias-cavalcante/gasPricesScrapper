

import requests

url = 'https://www.n1.is/umbraco/api/fuel/getfuelprices'

# Send the POST request
response = requests.post(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the JSON data from the response
    json_data = response.json()

    # Do something with the JSON data, such as print it to the console
    print(json_data[0])
else:
    print(f'Request failed with status code {response.status_code}')


def n1Data(resp):
    if response.status_code == 200:
        # Get the JSON data from the response
        json_data = resp.json()

    # Do something with the JSON data, such as print it to the console
        return json_data[0]
    else:
        return "IT has failed"

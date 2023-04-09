import requests
import json
from cityRegion import getRegionByCity


def fetch_data(url):
    response = requests.get(url)
    return response.json()


def filter_data(data, company_name):
    filtered_data = {}

    for result in data['results']:
        if result['company'] == company_name:
            name = result['name']
            region = getRegionByCity(name)
            bensin = result['bensin95']
            diesel = result['diesel']

            filtered_data[name] = {
                "region": region,
                "bensin": bensin,
                "diesel": diesel
            }

    return filtered_data


def main():
    url = "https://apis.is/petrol"
    company_name = "Orkan"

    data = fetch_data(url)
    filtered_data = filter_data(data, company_name)

    return json.dumps(filtered_data, ensure_ascii=False)

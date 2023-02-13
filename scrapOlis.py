import requests
from bs4 import BeautifulSoup


locations = []
okt95s = []
diesels = []


def cleanArray(array):
    cleaned = []
    if len(array) > 3:
        cleaned.append(array[0])
        cleaned.append(array[-2])
        cleaned.append(array[-1])
    elif len(array) < 3:
        return None
    else:
        return array
    return cleaned


# Make a request to the website
url = "https://www.olis.is/solustadir/thjonustustodvar/eldsneytisverd/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the  desired content on the page
    elements = soup.find_all("tr", {"class": "alt"})

    whiteElements = soup.find_all("tr", class_="")

    for l in elements:
        listed = l.text.split()
        cleansed = cleanArray(listed)
        print(cleansed)

    print("--------------------\n")

    for l in whiteElements:
        listed = l.text.split()
        cleansed = cleanArray(listed)
        print(cleansed)


else:
    print("Request failed with status code: ", response.status_code)

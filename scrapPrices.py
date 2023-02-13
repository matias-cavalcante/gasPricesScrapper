import requests
from bs4 import BeautifulSoup


def rejectEmptyString(row):
    numbers = '0123456789'
    numbersTotal = 0
    noEmpty = ""
    for c in range(len(row)):
        if row[c] != " ":
            noEmpty = noEmpty + row[c]
            if row[c] in numbers:
                numbersTotal = numbersTotal + 1
        if numbersTotal == 8:
            break
    return noEmpty


def findName(row):
    numbers = "0123456789"
    location = ""
    for c in range(len(row)):
        if row[c] not in numbers or row[c] == ',':
            location = location + row[c]
        else:
            break
    return location


locations = []
okt95s = []
diesels = []

# Make a request to the website
url = "https://www.orkan.is/orkustodvar/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the  desired content on the page
    elements = soup.find_all("div", {"class": "row accordion__row"})

    # Normalize the information to the desired format
    def cleanResults(cleaner, info):
        noSpaces = cleaner(info).split(" ")
        lastRefined = [noSpaces[0].strip()]
        return lastRefined

    for l in elements:
        toText = l.text
        cleaned = cleanResults(rejectEmptyString, toText)

        name = findName(cleaned[0])
        okt = cleaned[0][len(findName(cleaned[0]))
                             :len(findName(cleaned[0])) + 5]
        dsl = cleaned[0][len(findName(cleaned[0])) + 5:]
        print(name.upper(), " -- okt95/ ", okt, " -- diesel/ ", dsl)

    # Currently the information is only displayed, but eventually it will be returned in json format

else:
    print("Request failed with status code: ", response.status_code)

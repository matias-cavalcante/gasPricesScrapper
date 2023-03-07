import requests
from bs4 import BeautifulSoup
import cityRegion
import csv

# Make a request to the website
url = "https://www.orkan.is/orkustodvar/"
response = requests.get(url)


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

# Normalize the information to the desired format


def cleanResults(cleaner, info):
    noSpaces = cleaner(info).split(" ")
    lastRefined = [noSpaces[0].strip()]
    return lastRefined

# Handle results with hardcoded values (no other choice)


def hardcodeStationOrk(check):
    if check == 'miklabraut':
        return 'Miklabraut, norður'
    elif check == 'miklabrautv.kringluna':
        return 'Miklabraut, suður'
    elif check == 'kjarnagata,akureyri':
        return 'Akureyri, Kjarnagata'
    return check


if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all("div", {"class": "row accordion__row"})
    jsoningData = {}

    for l in elements:
        orkanData = {}
        toText = l.text
        cleaned = cleanResults(rejectEmptyString, toText)
        name = findName(cleaned[0]).lower()
        name = hardcodeStationOrk(name)
        region = cityRegion.getRegionByCity(name)
        okt = float(cleaned[0][len(findName(cleaned[0])):len(
            findName(cleaned[0])) + 5].replace(',', '.'))
        dsl = float(
            cleaned[0][len(findName(cleaned[0])) + 5:].replace(',', '.'))
        orkanData['region'] = region
        orkanData['bensin'] = okt
        orkanData['disel'] = dsl
        jsoningData[name] = orkanData

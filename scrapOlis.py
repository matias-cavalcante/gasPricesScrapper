import requests
from bs4 import BeautifulSoup

from cityRegion import getRegionByCity


url = "https://www.olis.is/solustadir/thjonustustodvar/eldsneytisverd/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

darkRowStations = soup.find_all("tr", {"class": "alt"})
lightRowStations = soup.find_all("tr", class_="")
lightRowStations = lightRowStations[2:]


def cleanArray(array):
    cleaned = []
    if len(array) >= 3:
        cleaned.append(array[0])
        cleaned.append(array[-2])
        cleaned.append(array[-1])
        return cleaned


def stationDictFiller(dictionary, elements):
    updatedDictionary = dictionary
    for row in elements:
        rowText = row.text.split()
        if type(rowText) == list:
            cleanRows = cleanArray(rowText)
            stationName = cleanRows[0].lower().replace(',', '')
            bensin = float(cleanRows[1].replace(',', '.'))
            disel = float(cleanRows[2].replace(',', '.'))
            updatedDictionary[stationName] = {'region': getRegionByCity(stationName),
                                              'bensin': bensin, 'disel': disel}
    return updatedDictionary


stationsJsoned = {}
darkStationsInDict = stationDictFiller(stationsJsoned, darkRowStations)
totalStationsInDict = stationDictFiller(darkStationsInDict, lightRowStations)

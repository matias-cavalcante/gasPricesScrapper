import requests
from dataN1 import clearNameStation
from cityRegion import getRegionByCity

url = 'https://www.atlantsolia.is/umbraco/api/service/GetAllFuelPrices'
response = requests.get(url)


def removeFirstPosWhiteSpace(spaced):
    if spaced.startswith(" "):
        return spaced.lstrip()
    return spaced


def hardcodeNamesForAO(check):
    if check == ' Háaleiti':
        return 'Háaleitisbraut'
    elif check == 'Kópavogur Skemmuvegur':
        return 'Skemmuvegur'
    return check

# When consuming the API the name for ' Háaleiti' does not work with my file, so i replace it for 'Háaleitisbraut'


def stationsAndPricesAO(resp):
    dataNeeded = {}
    dataRaw = resp.json()
    actualData = dataRaw['items']
    for data in actualData:
        stationData = {}
        stationName = clearNameStation(data['name'])
        stationName = hardcodeNamesForAO(stationName)
        stationName = removeFirstPosWhiteSpace(stationName)
        stationData['region'] = getRegionByCity(stationName)
        stationData['bensin'] = data['oct95']
        stationData['disel'] = data['diesel']
        dataNeeded[stationName] = stationData
    return dataNeeded

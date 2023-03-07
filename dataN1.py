from cityRegion import getRegionByCity
import requests

url = 'https://www.n1.is/umbraco/api/fuel/getfuelprices'
response = requests.post(url)


def clearNameStation(name):
    if len(name) > 2:
        splittedName = name.split('-')
        return splittedName[-1]
    else:
        return name


def removeFirstPosWhiteSpace(spaced):
    if spaced.startswith(" "):
        return spaced.lstrip()
    return spaced


def hardcodeStationN1(check):
    if check == 'Lækjargata':
        return 'Lækjargata - Hafnarfjörður'
    elif check == 'Þjónustustöð Höfn':
        return 'Höfn'
    return check


def stationsAndPrices(resp):
    json_data = response.json()
    dataNeeded = {}
    for data in json_data:
        stationData = {}
        stationName = clearNameStation(data['Name'])
        if stationName[0] == " ":
            stationName = stationName[1:]
        stationName = removeFirstPosWhiteSpace(stationName)
        stationName = hardcodeStationN1(stationName)
        stationData['region'] = getRegionByCity(stationName)
        stationData['bensin'] = float(data['GasPrice'].replace(',', '.'))
        stationData['disel'] = float(data['DiselPrice'].replace(',', '.'))
        dataNeeded[stationName] = stationData
    return dataNeeded

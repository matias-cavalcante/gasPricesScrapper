import requests
from dataN1 import clearNameStation

from cityRegion import getRegionByCity

url = 'https://www.ob.is/resources/getprices2.aspx'
response = requests.get(url)


def replaceFaultyName(checkme):
    if checkme == 'ÓB Sauðárkókur':
        return 'Sauðárkrókur'
    return checkme


def hardcodeStationOB(check):
    if check == 'Melabraut':
        return 'Melabraut, Hafnarfirði'
    return check


def stationsAndPrices(resp):
    dataNeeded = {}
    dataRaw = resp.json()
    for data in dataRaw:
        if data['Name'] == 'Bryggjudaela':
            pass
        else:
            stationData = {}
            stationName = replaceFaultyName(clearNameStation(data['Name']))
            stationName = hardcodeStationOB(stationName)
            region = getRegionByCity(stationName)
            stationData['region'] = region
            stationData['bensin'] = float(data['PricePetrol'])
            stationData['disel'] = float(data['PriceDiesel'])
            dataNeeded[stationName] = stationData
    return dataNeeded

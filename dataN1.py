import requests

url = 'https://www.n1.is/umbraco/api/fuel/getfuelprices'
response = requests.post(url)


def clearNameStation(name):
    if len(name) > 2:
        splittedName = name.split('-')
        return splittedName[-1]
    else:
        return name


def stationsAndPrices(resp):
    dataNeeded = {}
    for data in json_data:
        stationData = {}
        stationName = clearNameStation(data['Name'])
        stationData['gas'] = data['GasPrice']
        stationData['diesel'] = data['DiselPrice']
        dataNeeded[stationName] = stationData
    return dataNeeded

from cityRegion import getRegionByCity
import requests

def get_n1_prices_data():
    url = 'https://gamli.n1.is/umbraco/api/fuel/getfuelprices'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://gamli.n1.is/thjonusta/eldsneyti/daeluverd/"
    }
    try:
        response = requests.post(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching N1 data: {e}")
        return []


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


def stationsAndPricesN1(resp=None):
    json_data = get_n1_prices_data()
    dataNeeded = {}
    for data in json_data:
        stationData = {}
        stationName = clearNameStation(data['Name'])
        if stationName and stationName[0] == " ":
            stationName = stationName[1:]
        stationName = removeFirstPosWhiteSpace(stationName)
        stationName = hardcodeStationN1(stationName)
        stationData['region'] = getRegionByCity(stationName)
        if data.get('GasPrice') is not None and data.get('DiselPrice') is not None:
            stationData['bensin'] = float(data['GasPrice'].replace(',', '.'))
            stationData['disel'] = float(data['DiselPrice'].replace(',', '.'))
            dataNeeded[stationName] = stationData
    return dataNeeded

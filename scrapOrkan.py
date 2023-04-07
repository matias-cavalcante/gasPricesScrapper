import re
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from cityRegion import getRegionByCity


def process_string(tup):
    name = tup[0]
    cleanedName = ""
    nameExclude = "0123456789,"
    for p in name:
        if p not in nameExclude:
            cleanedName = cleanedName + p
    return cleanedName


def getNumbers(tup):
    references = "0123456789"
    singleNumber = tup[1]
    capturedNumbers = ""
    for n in tup[0]:
        if n in references:
            capturedNumbers = capturedNumbers + n
    group1 = capturedNumbers[0:3] + "." + capturedNumbers[3]
    group2 = capturedNumbers[4:7] + "." + singleNumber
    return [group1, group2]


def main():
    url = "https://www.orkan.is/orkustodvar/"

    session = HTMLSession()
    response = session.get(url)
    response.html.render(timeout=6, sleep=4)

    content = response.html.raw_html

    soup = BeautifulSoup(content, "html.parser")
    collapse_panel = soup.find('div')

    try:
        raw_data = collapse_panel.text
    except AttributeError:
        return "Not available"

    pattern = r'(?<=[\s])([ÞA-Z][a-zA-ZáéíóúýÁÉÍÓÚÝæÆöÖð, \d]*,[a-zA-ZáéíóúýÁÉÍÓÚÝæÆöÖ\d]*,)(\d{1,8})'
    matches = re.findall(pattern, raw_data)

    storeData = {}
    for m in matches:
        stationInfo = {}
        stationInfo['region'] = getRegionByCity(process_string(m))
        stationInfo['bensin'] = float(getNumbers(m)[0])
        stationInfo['disel'] = float(getNumbers(m)[1])
        storeData[process_string(m)] = stationInfo

    return storeData


print(main())

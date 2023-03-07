
import csv
import os
from unidecode import unidecode
import re


def removeAccent(word):
    word = word.lower()
    modified = re.sub(r'[áéíóúý]', lambda m: {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ý": "y"}[m.group(0)], word)
    firstUpper = modified[0].upper()
    return firstUpper + modified[1:]


def last_char_differs(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if i == len(str1) - 1 and str1[i] != str2[i]:
            return str1[0:-2] + 'i'
        elif str1[i] != str2[i]:
            return False
    return False


def getRegionByCity(city_name):
    toCheck = removeAccent(city_name)
    csv_file = 'C:/Users/35476/Desktop/gas/iceland.csv'
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            candidate = removeAccent(row['location'])
            if candidate == toCheck:
                return row['region']
            elif candidate in toCheck or toCheck.lower() in candidate:
                return row['region']
            elif " " in candidate:
                candidate = candidate.split(" ")
                if candidate[1].lower() == toCheck.lower():
                    return row['region']
            elif last_char_differs(toCheck.lower(), candidate.lower()) != False:
                return row['region']
    return None

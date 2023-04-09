

import difflib
import csv
import os
import re


def removeAccent(word):
    word = word.lower()
    modified = re.sub(r'[áéíóúý]', lambda m: {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ý": "y"}[m.group(0)], word)
    firstUpper = modified[0].upper()
    return firstUpper + modified[1:]


def load_city_regions():
    city_regions = {}
    csv_file = 'iceland.csv'

    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city_name = removeAccent(row['location'])
            region = row['region']
            city_regions[city_name] = region

    return city_regions


city_regions = load_city_regions()


def getRegionByCity(city_name):
    toCheck = removeAccent(city_name)

    # Find the most similar city using SequenceMatcher
    most_similar_city = max(city_regions, key=lambda x: difflib.SequenceMatcher(
        None, toCheck.lower(), x.lower()).ratio())

    return city_regions[most_similar_city]

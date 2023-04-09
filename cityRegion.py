

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


city_region_dict = load_city_regions()


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def getRegionByCity(city_name):
    toCheck = removeAccent(city_name)

    # Find the most similar city using Levenshtein distance
    most_similar_city = max(city_region_dict.items(
    ), key=lambda x: -levenshtein_distance(toCheck.lower(), x[0].lower()))

    return most_similar_city[1]


print(getRegionByCity('Fjarðarkaup'))

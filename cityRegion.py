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


def getRegionByCity(city_name):
    toCheck = removeAccent(city_name)
    max_similarity = 0
    best_region = None

    for candidate, region in city_region_dict.items():
        # If the candidate matches the city_name exactly, return the region immediately
        if candidate == toCheck:
            return region

        # Check if the candidate is contained in the city_name or vice versa
        if candidate in toCheck or toCheck.lower() in candidate:
            similarity = difflib.SequenceMatcher(
                None, toCheck.lower(), candidate.lower()).ratio()

            if similarity > max_similarity:
                max_similarity = similarity
                best_region = region

    # If no exact or partial match is found, use SequenceMatcher for more precise matching
    if best_region is None:
        most_similar_city = max(city_region_dict.keys(), key=lambda x: difflib.SequenceMatcher(
            None, toCheck.lower(), x.lower()).ratio())
        best_region = city_region_dict[most_similar_city]

    return best_region

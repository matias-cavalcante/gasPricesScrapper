
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
    csv_file = 'iceland.csv'
    cities = []

    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            candidate = removeAccent(row['location'])
            cities.append((candidate, row['region']))

    # Find the most similar city using SequenceMatcher
    most_similar_city = max(cities, key=lambda x: difflib.SequenceMatcher(
        None, toCheck.lower(), x[0].lower()).ratio())

    return most_similar_city[1]

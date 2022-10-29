# ! python 3.8.10
# combaineCsvs.py- combines all csv files stripped off their headers into one file

import os
import csv


def find_all_csv():
    csvFiles = []

    for filename in os.listdir('./headerRemoved'):
        if filename.endswith('.csv'):
            csvFiles.append(filename)

    return csvFiles


def combine_all_csvs():
    csvFiles = find_all_csv()

    csvWriter = csv.writer(
        open('headerRemoved/allCsv.csv', 'w'))

    for filename in csvFiles:
        csvFileObj = open(filename)
        csvReader = csv.reader(csvFileObj)

        for row in csvReader:
            csvWriter.writerow(row)
    print('Files were combined into allCsv.csv file')

# combine_all_csvs()

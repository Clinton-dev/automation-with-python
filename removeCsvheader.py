#! python 3.8.10
# removeCsvHeader.py - Removes the header from all csv files in current directory

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)

    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    print('Removed header from ' + csvFilename + '...')

    csvFileObj = open(os.path.join(
        'headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)

    csvFileObj.close()

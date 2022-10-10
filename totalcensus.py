# ! python3.8.10
import pprint
import openpyxl
# Reads the data from the Excel spreadsheet
print("***Opening File***")
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
# print(sheet)
country = {}
print("***Reading File***")

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['c' + str(row)].value
    pop = sheet['D' + str(row)].value
    country.setdefault(state, {})
    country[state].setdefault(county, {'pop': 0, 'track': 0})
# Counts the number of census tracts in each county
    country[state][county]['track'] += 1
# Counts the total population of each county
    country[state][county]['pop'] += int(pop)
print('***Writing to file***')
file = open('newcensus2010.py', 'w')
file.write('allData = ' + pprint.pformat(country))
file.close()
print('***Closing to file***')

# Prints the results

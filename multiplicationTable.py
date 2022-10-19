#! python3.8.10

""" multiplicationTable.py - takes a number N from the command line and creates an N * N table in Excel spreadSheet """
# Get the number of the users input from the terminal
# create workbook object
# create a loop that runs n number of times
# Each time creating a row filed with details
# save the workbook as multiplicationTable.xlsx
import openpyxl
import string
n = int(input('Enter number you want your table to be:'))

alphabet = list(string.ascii_uppercase)
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Multiplication table'

for i in range(1, n+1):
    # write to one column of the sheet
    cell_name = f'{alphabet[i]}{i}'
    sheet[cell_name] = i
    # for e in range(1,n+1):
    #     print(e)


wb.save('multiplicationTable.xlsx')

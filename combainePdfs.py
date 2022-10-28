#! python 3.8.10
""" Combaine all pdfs in working directory into one file """

import PyPDF2
import os


def find_pdffiles():
    pdfFiles = []

    for filename in os.listdir():
        if filename.endswith('.pdf'):
            pdfFiles.append(filename)

    pdfFiles.sort(key=str.lower)
    return pdfFiles


def combine_pdf():
    pdfFiles = find_pdffiles()

    pdfWriter = PyPDF2.PdfFileWriter()

    for pdfFile in pdfFiles:
        file = open(pdfFile, 'rb')
        path = file.name
        # check to see if file is not empty
        if (os.stat(file.name).st_size != 0):
            pdfReader = PyPDF2.PdfFileReader(file.name)

            # check to see if file is decrypted
            if (pdfReader.isEncrypted):
                print(f'{path} is encrypted')
            else:
                for pageNum in range(pdfReader.numPages):
                    if pageNum != 0:
                        pdfWriter.addPage(pdfReader.getPage(pageNum))

    resultPdf = open('allminutes.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
    print("***Finished combaning pdf Files***")
    print(f"check allminutes.pdf")


# combine_pdf()

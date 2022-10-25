#! python 3.8.10
# reads a word document and returns only text

import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for par in doc.paragraphs:
        fullText.append(par.text)

    return '\n'.join(fullText)


print(getText('demo.docx'))

# ! python3.8.10
"""
    launches map in browser using an address from the command line of clipboard
"""

import webbrowser
import pyperclip
import sys

if len(sys.argv) > 1:
    # Read command line arguments from sys.argv
    address = ' '.join(sys.argv[1:])

else:
    # read clipboard contents
    address = pyperclip.paste()

# call webbrowser.open to open web browser
webbrowser.open('https://www.google.com/maps/place/' + address)

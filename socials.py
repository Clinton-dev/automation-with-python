#! python3.8.10

"""
An application that opens my most visited social media sites
"""
import sys
import webbrowser
# get social name
facebook = 'https://www.facebook.com/'
twitter = 'https://twitter.com/home'
instagram = 'https://www.instagram.com/'
github = 'https://github.com/'
whatsapp = 'https://web.whatsapp.com/'

if (len(sys.argv) > 1):
    social = ''.join(sys.argv[1:])
    if (social == 'facebook' or social == 'fb'):
        webbrowser.open(facebook)
    elif (social == 'twitter'):
        webbrowser.open(twitter)
    elif (social == 'instagram' or social == 'insta'):
        webbrowser.open(instagram)
    elif (social == 'github' or social == 'gh'):
        webbrowser.open(github)
    elif (social == 'whatsapp' or social == 'wa'):
        webbrowser.open(whatsapp)

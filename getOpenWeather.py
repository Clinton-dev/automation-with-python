#! python 3.8.10
# getOpenWeather.py - a program that downloads the weather forecast for the
# next few days and printed it as plaintext.
import sys
import requests
import json
APPID = '812e47164b26a94bd6102f8eb0f2a94b'


if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py cityname, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.arg[1:])

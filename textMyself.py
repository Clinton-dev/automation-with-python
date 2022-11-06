#! python3.8.10
#  textMyself.py - Defines the textmyself() function that text a msg that is passed to it as a string
# How to use
# 1. import textMyself
# 2. textMyself.textmyself('The boring task is finished')

from twilio.rest import Client
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Find .envfile

accountSID = os.getenv('ACCOUNTSID')
authToken = os.getenv('AUTHTOKEN')
twilioNumber = os.getenv('TWILIONUMBER')
myNumber = os.getenv('MYNUMBER')


def textmyself(msg):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=msg, from_=twilioNumber, to=myNumber)


# textmyself('enda ulale')

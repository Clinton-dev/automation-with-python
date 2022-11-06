#! python3.8.10
#  textMyself.py - Defines the textmyself() function that text a msg that is passed to it as a string
# How to use
# 1. import textMyself
# 2. textMyself.textmyself('The boring task is finished')

from twilio.rest import Client
# TODO: add this to env file
accountSID = 'ACb133f3644df59463028eb7d6b95dd5e6'
authToken = 'a4cfabf081d617bd68972cc9d4cabaa2'
twilioNumber = '+19472104607'
myNumber = '+254703442841'


def textmyself(msg):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=msg, from_=twilioNumber, to=myNumber)

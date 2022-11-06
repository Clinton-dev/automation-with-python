#! python3.8.10
#  textMyself.py - Defines the textmyself() function that text a msg that is passed to it as a string
# How to use
# 1. import textMyself
# 2. textMyself.textmyself('The boring task is finished')

from twilio.rest import Client
# TODO: add this to env file
accountSID = ''
authToken = ''
twilioNumber = '+1'
myNumber = '+254'


def textmyself(msg):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=msg, from_=twilioNumber, to=myNumber)

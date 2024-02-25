# Sending SMS
# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

def sendSms(phone_number,message):
    
    # the following line needs your Twilio Account SID and Auth Token
    client = Client("AC7ca044a86ed292243b4f8d33a61af95d", "eeb996293dc40440241f262628156ef1")
    
    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to = "+91"+phone_number, 
                           from_ = "+14144551648", 
                           body = message)
    
    print("Message Sent")
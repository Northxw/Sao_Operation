# -*- coding:utf-8 -*-
from twilio.rest import Client

# The value of the following authentication information can be found in your twilio account.
account = 'account_sid'
token = 'auth_token'
client = Client(account, token)

message = client.messages.create(
    to='+86132****3305',        # Your phone number
    from_='+1 541 403 9876',    # Your twilio number
    body="This is a FoLeng! Haha..."    # SMS content to be sent
)

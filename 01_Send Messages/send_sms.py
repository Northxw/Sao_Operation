# -*- coding:utf-8 -*-
from twilio.rest import Client

account = 'AC7a5ec45b5b97ed9b4338125b90c7e6aa'
token = 'fb17167e075cb2577ca1dbd0df31076d'
client = Client(account, token)

message = client.messages.create(
    to='+8613201723305',
    from_='+1 541 403 9876',
    body="This is a FoLeng! Haha..."
)
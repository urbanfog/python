from twilio.rest import Client
import os


class TwilioSMS:
    def __init__(self):
        self.twilio_account_sid = ENV_VAR
        self.twilio_auth_token = ENV_VAR
        self.client = Client(self.twilio_account_sid, self.twilio_auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_='+18648062131',
            to='+15879991663'
        )
        print(message.status)

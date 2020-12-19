from twilio.rest import Client
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')

    def send_sms(self, message, phone_number):
        client = Client(self.twilio_account_sid, self.twilio_auth_token)
        message = client.messages.create(
            body=message,
            from_='+18648062131',
            to=phone_number
        )
        print(message)

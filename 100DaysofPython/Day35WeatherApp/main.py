import requests
from twilio.rest import Client
import os


MY_LAT = 51.048615
MY_LONG = -114.070847
twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    # only want 48 hour forecast
    "exclude": "current,minutely,daily",
    "appid": "cd62c103a3cd8c421242dc78cbfcb9ef",
    "units": "metric",
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
data = response.json()
hourly_data = data['hourly']
bring_umbrella = False

for hour in hourly_data[0:12]:
    if int(hour['weather'][0]['id']) < 700:
        bring_umbrella = True


def send_sms():
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages \
                    .create(
                        body="Hey baby, hope we meet up at xiron again soon. ❤️",
                        from_='+18648062131',
                        to='+15879991663'
                    )
    print(message.status)


if bring_umbrella:
    send_sms()
else:
    print('No umbrella today')

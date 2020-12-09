from Day32Email.main import MY_EMAIL, MY_PASSWORD
import requests
import datetime as dt
import smtplib

MY_LAT = 51.048615
MY_LONG = -114.070847
MY_EMAIL = ""
MY_PASSWORD = ""


def iss_nearby():
    iss_data = requests.get("http://api.open-notify.org/iss-now.json").json()
    iss_data.raise_for_status()
    iss_lat = float(iss_data['iss_position']['latitude'])
    iss_long = float(iss_data['iss_position']['longitude'])

    if MY_LAT < (iss_lat + 5) and MY_LAT > (iss_lat - 5):
        if MY_LONG < (iss_long + 5) and MY_LONG > (iss_long - 5):
            print('nearby')
            return True
        else:
            print('Still working but not nearby')
            return False
    else:
        print('Still working but not nearby')
        return False


def is_dark_outside():
    params = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }
    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    time_zone = 7
    sunrise = int(data['results']['sunrise'].split("T")
                  [1].split(":")[0]) - time_zone
    sunset = int(data['results']['sunset'].split("T")
                 [1].split(":")[0]) - time_zone
    time_now = dt.datetime.now().hour
    if time_now >= sunset:
        print("Nighttime")
        return True
    else:
        print("Daytime")
        return False


def send_email():
    msg = f"Subject: LOOK UP! ISS is overhead."

    with smtplib.SMTP("smtp.live.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=msg)


if iss_nearby():
    if is_dark_outside():
        send_email()

import smtplib
import datetime as dt
import random
import pandas as pd


MY_EMAIL = "my email"
MY_PASSWORD = "my password"

now = dt.datetime.now()
current_day = now.day
current_month = now.month
birthdays = pd.read_csv('birthdays.csv')
todays_birthdays = birthdays[birthdays['month'] == current_month]


def send_email(message, send_to):
    msg = f"Subject: Happy Birthday!\n\n{message}".encode(encoding="utf8")
    with smtplib.SMTP("smtp.live.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=send_to,
                            msg=msg)


def _choose_template():
    ltr_num = random.randint(1, 3)
    with open(f"letter_templates/letter_{ltr_num}.txt", mode="r") as letter:
        return letter.read()


def draft_and_send_email():
    for label, row in todays_birthdays.iterrows():
        name = row['name']
        email = row['email']
        ltr = _choose_template().replace("[NAME]", f"{name}")
        send_email(ltr, email)


draft_and_send_email()

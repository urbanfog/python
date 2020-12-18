from sheety import Sheety
from nutrionix import Nutrionix
import datetime as dt


exercise = input("What exercise did you do? ")

nutri = Nutrionix(query=exercise, gender="male",
                  weight=100, height=180, age=37)

# Post data to Nutrionix and receive json
data = nutri.post()['exercises'][0]

# Create Sheety object and post data
sheety = Sheety(date=dt.datetime.now().date(),
                time=dt.datetime.now().time(),
                exercise=data['user_input'].title(),
                duration=data['duration_min'],
                calories=data['nf_calories'],
                )
sheety.post()

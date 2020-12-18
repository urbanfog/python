import requests


class Sheety:

    def __init__(self, date, time, exercise, duration, calories) -> None:
        self.endpoint = f"SHEETY_PAGE"
        self.header = {
            "Authorization": f"Bearer {TOKEN}}"
        }
        self.date = date
        self.time = time
        self.exercise = exercise
        self.duration = duration
        self.calories = calories

    def post(self):
        params = {
            "workout": {
                "date": self.date.strftime("%d/%m/%Y"),
                "time": self.time.strftime("%I:%M:%S"),
                "exercise": self.exercise,
                "duration": self.duration,
                "calories": self.calories,
            }
        }
        post = requests.post(
            url=self.endpoint, json=params, headers=self.header)
        post.raise_for_status()
        print(post)

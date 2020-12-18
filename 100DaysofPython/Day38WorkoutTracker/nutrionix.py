import requests


class Nutrionix:
    def __init__(self, query: str, gender: str, weight: int, height: int, age: int) -> None:
        self.end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.header = {
            "x-app-id": APP_ID,
            "x-app-key": APP_KEY,
        }

        self.params = {
            "query": query,
            "gender": gender,
            "weight_kg": weight,
            "height_cm": height,
            "age": age,
        }

    def post(self):
        post = requests.post(
            self.end_point, json=self.params, headers=self.header)
        post.raise_for_status()
        json = post.json()
        return(json)

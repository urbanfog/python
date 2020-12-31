import requests
import pandas as pd

df = pd.read_csv("countries.csv")


class Person:
    def __init__(self, name: str):
        self.name = name
        self.params = {'name': self.name}
        self.country = self.get_country()
        self.age = self.get_age()
        self.gender = self.get_gender()

    def get_country(self):
        response = requests.get(
            "https://api.nationalize.io", params=self.params).json()
        country_code = response['country'][0]['country_id']
        return df[df.Code ==
                  country_code]['Name'].to_string(index=False)

    def get_age(self):
        response = requests.get("https://api.agify.io",
                                params=self.params).json()
        return response['age']

    def get_gender(self):
        response = requests.get(
            "https://api.genderize.io", params=self.params).json()
        return response['gender']

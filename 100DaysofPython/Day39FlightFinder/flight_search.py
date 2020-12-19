from flight_data import FlightData
import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv('TEQUILA_KEY')


class FlightSearch():
    # This class is responsible for talking to the Flight Search API.
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "CAD"
        }
        end_point = f"TEQUILA_ENDPOINT/v2/search"
        response = requests.get(end_point=end_point,
                                params=query, headers=header)
        data = response.json()["data"][0]

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data

    def get_destination_code(self, city) -> str:
        end_point = f"{TEQUILA_ENDPOINT}/locations/query"
        header = {"apikey": TEQUILA_API_KEY}
        query = {
            "term": city,
            "location_types": "city",
        }
        response = self.get(url=end_point,
                            params=query, headers=header)
        results = response.json()['locations'][0]['code']
        return results

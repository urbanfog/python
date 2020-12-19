import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/2b88e7d917e876a13a31c8e3c16af4a1/flightDeals/prices"


class DataManager():
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(
                url=f"SHEETY_PRICES_ENDPOINT/+{city['id']}", json=new_data)
            print(response.text)

    # def update(self, index, city, iata, lowest_price):
    #     end_point = f"/{index}"
    #     params = {
    #         "price": {
    #             "city": city,
    #             "iataCode": iata,
    #             "lowestPrice": lowest_price,
    #         }
    #     }
    #     update = requests.put(
    #         url=self.url+end_point, json=params, headers=self.header)
    #     update.raise_for_status()
    #     print(update)

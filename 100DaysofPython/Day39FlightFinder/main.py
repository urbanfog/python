# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

# Pull data from Sheety
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY = 'YYC'

# Check for missing IATA codes & fill missing items
if sheet_data[0]['iataCode'] == "":
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Check destinations for new low prices
for destination in sheet_data:
    flight = flight_search.check_flights(
        city=ORIGIN_CITY,
        destination=destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    if flight.price < destination['lowestPrice']:
        notification_manager.send_sms(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}:{flight.origin_airport} -> {flight.destination_city}: {flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
        )

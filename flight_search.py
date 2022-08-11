import datetime
import os
import requests

# import environmental variables
Tequilla_Affill_ID = os.environ.get("AFFILL_ID")
Tequilla_API_KEY = os.environ.get("API_KEY")
tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:

    """
        Gets current flight data from Kiwi.com using the Tequila API.
        Provides helper functions to get current date and determine offset_date.
    """

    def __init__(self, flight_from, flight_to, week_range, price_to, min_return_time_days, max_return_time_days,
                 stop_overs):

        """
            Updates object with flight data from Kiwi.com using the Tequila API
                Parameters:
                    flight_from (str): Current location.
                    flight_to (str):  Destination location.
                    week_range (int): Interval in weeks from current date in which to search flight information.
                    price_to (int) : Maximum flight price to search.
                    min_return_time_days (int): Shortest interval allowed between arrival and return flight.
                    max_return_time_days (int): Longest interval allowed between arrival and return flight.
                    stop_overs (int): Number of connecting flights allowed.
        """

        # get current date
        today = datetime.date.today()
        formatted_today = today.strftime("%d/%m/%Y")

        # get offset date
        offset_date = today + datetime.timedelta(weeks=week_range)
        formatted_offset_date = offset_date.strftime("%d/%m/%Y")

        header = {
            "apikey": Tequilla_API_KEY
        }

        tequila_params = {
            "fly_from": flight_from,
            "fly_to": flight_to,
            "date_from": formatted_today,
            "data_to": formatted_offset_date,
            "price_to": price_to,
            "one_for_city": 1,
            "curr": "USD",
            "nights_in_dst_from": min_return_time_days,
            "nights_in_dst_to": max_return_time_days,
            "flight_type": "round",
            "max_stopovers": stop_overs,
        }

        self.__response = requests.get(url=tequila_endpoint, params=tequila_params, headers=header)

    def get_flight_data(self):

        """
            Get one available flights for current flight object if price is lower than reference max price.
                Return:
                    self.__response (json): Returns available flight data from Tequila API
        """

        return self.__response.json()


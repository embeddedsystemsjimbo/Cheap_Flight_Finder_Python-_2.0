import requests


class UpdateFlightDealUser:

    """
        Registers firstname, lastname and email to Google Sheets Document using Sheety API
            Parameter:
                    first_name (str) : User's first name
                    last_name (str) : User's last name
                    email (str) : User's last name
    """

    def __init__(self, first_name, last_name, email):

        # endpoint url to add to your google sheet
        flight_user_endpoint = "https://api.sheety.co/7c81d9be8a3fc40fb73b464d6005dd73/flightDeals/sheet1"

        header = {
            "Authorization": "Bearer OA9lv5j9VFO#",
            "Content_Type": "application/json"
        }

        # Sheety camelCases all JSON keys, so a header named "First Name" will become "firstName".
        sheety_params = {
            "sheet1": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }

        response = requests.post(url=flight_user_endpoint, json=sheety_params, headers=header)

        print(response.text)

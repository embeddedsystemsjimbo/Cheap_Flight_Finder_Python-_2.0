import requests
import os


HEADER = {
    "Authorization": os.environ.get("SHEETY_API_KEY"),  # import environmental variable
    "Content_Type": "application/json"
}


class DataManager:

    """
        GET reference flight information and POST new user information to/from Google Sheets documents using Sheety API.
    """

    @staticmethod
    def get_city_list():

        """
        Get list potential travel destinations from Google Sheets Document using Sheety API.

            Return: city_list (list-dict): Returns potential destination cities, destination IATA
                                                city codes and  lowest flight prices.
        """

        flights_endpoint = "https://api.sheety.co/c94a37da3d2003455b7481485ad51b7d/flightDeals/sheet1"

        response = requests.get(url=flights_endpoint, headers=HEADER).json()

        city_list = [city for city in response["sheet1"]]

        return city_list

    @staticmethod
    def register_new_user(first_name, last_name, email):

        """
              Registers firstname, lastname and email to Google Sheets Document using Sheety API
                  Parameter:
                          first_name (str) : User's first name.
                          last_name (str) : User's last name.
                          email (str) : User's last name.
          """

        users_endpoint = "https://api.sheety.co/c94a37da3d2003455b7481485ad51b7d/flightUsers/sheet1"

        # Sheety camelCases all JSON keys, so a header named "First Name" will become "firstName".

        sheety_params = {
            "sheet1": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }

        response = requests.post(url=users_endpoint, json=sheety_params, headers=HEADER)

    @staticmethod
    def get_user_list():

        """
            Get list of users registered with flight club.
                Returns:
                    response (list-dict) : Return registered user data including First_Name, Last_Name and Email.
        """

        user_list_endpoint = "https://api.sheety.co/c94a37da3d2003455b7481485ad51b7d/flightUsers/sheet1"

        response = requests.get(url=user_list_endpoint, headers=HEADER).json()

        user_list = [user for user in response["sheet1"]]

        return user_list



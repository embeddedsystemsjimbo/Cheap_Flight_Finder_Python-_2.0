from notification_manager import NotificationManager
from data_manager import DataManager
from flight_data import FlightData
from logo import logo

WEEK_OFFSET = 24  # search interval in weeks ~ 6 months.
MIN_RETURN_TIME_DAYS = 7  # 7 days min trip length
MAX_RETURN_TIME_DAYS = 30  # 30 days max trip length
CURRENT_LOCATION = "LON"  # London GB city code ...default location.

app_is_running = True


def get_flight_data():

    """
        Get most current flight data from kiwi.com using the Tequila API.
        Construct flight messages to send to flight club users.
    """

    # get data from Google Sheets Reference Flight List
    reference_flight_data = DataManager.get_city_list()

    # get current available flights with prices
    current_flight_data = FlightData(reference_flight_data_container=reference_flight_data,
                                     current_location=CURRENT_LOCATION,
                                     date_offset_in_week=WEEK_OFFSET,
                                     min_return_time_days=MIN_RETURN_TIME_DAYS,
                                     max_return_time_days=MAX_RETURN_TIME_DAYS).get_flight_data()

    for current_fight in current_flight_data:

        if len(current_fight['route']) == 3:

            message = f"Low Price alert! Only ${current_fight['price']}US to fly from " \
                      f"{current_fight['from_location']}-{current_fight['from_IATA']} to " \
                      f"{current_fight['to_location']}-{current_fight['to_IATA']} non" \
                      f"-direct through {current_fight['route'][0]['cityTo']}-" \
                      f"{current_fight['route'][0]['cityCodeTo']}  " \
                      f"{current_fight['route'][0]['local_departure']} at time " \
                      f"{current_fight['route'][0]['local_departure_time']} to "  \
                      f"{current_fight['route'][2]['local_departure']} at time " \
                      f"{current_fight['route'][2]['local_departure_time']}. \n\n" \
                      f"{current_fight['link']}"

        else:

            message = f"Low Price alert! Only ${current_fight['price']}US to fly direct from " \
                      f"{current_fight['from_location']}-{current_fight['from_IATA']} to " \
                      f"{current_fight['to_location']}-{current_fight['to_IATA']} between " \
                      f"{current_fight['route'][0]['local_departure']} at time " \
                      f"{current_fight['route'][0]['local_departure_time']} to " \
                      f"{current_fight['route'][1]['local_departure']} at time " \
                      f"{current_fight['route'][1]['local_departure_time']}. \n\n" \
                      f"{current_fight['link']}"

        send_email(message)


def send_email(message):

    """
         Email new flight deals to all flight club members.
            Parameter:
                message (str): Flight club deal message.
    """

    for user in DataManager.get_user_list():
        NotificationManager.email_user(user["firstName"], user["lastName"], user["email"], message)


while app_is_running:
    print(logo)
    print("\n\nWelcome to Brandon's Flight Club. \n"
          "We find the best flight deals and email you.")

    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")

    email_registration_is_running = True

    while email_registration_is_running:

        email_initial = input("What is your email? ")
        email_final = input("Type your email again ")

        if email_initial == email_final:

            print("You're in the club")
            print("Searching for flights...Please wait...")
            email_registration_is_running = False
            DataManager.register_new_user(first_name, last_name, email_final)
            get_flight_data()
            print("Finished searching ... check your email ")

        else:
            print("The email addresses you've provided don't match...try again")

    to_continue = input("Do you want to register another user? Yes or No ").lower()

    if to_continue == "no":
        app_is_running = False

from flight_search import FlightSearch


class FlightData:

    """
        Provides helper methods to get and organize reference and flight data.
    """

    def __init__(self, reference_flight_data_container, current_location, date_offset_in_week, min_return_time_days,
                 max_return_time_days):

        """
            Updates object with most current flight data for no stopovers and one stopover flights.
                Parameters:
                    reference_flight_data_container (DataManger): Reference Flight Data object.
                    current_location (str): Current city location IATA code.
                    date_offset_in_week (int): Interval in weeks from current date in which to search flight info.
                    min_return_time_days (int): Shortest interval allowed between arrival and return flight.
                    max_return_time_days (int): Longest interval allowed between arrival and return flight.
        """

        self.__reference_flight_data_container = reference_flight_data_container
        self.__current_location = current_location
        self.__date_offset_in_week = date_offset_in_week
        self.__min_return_time_days = min_return_time_days
        self.__max_return_time_days = max_return_time_days

        # list of new low priced flights
        self.__destination_price_list = []

        # for each destination found in google sheets document
        for ref_destination in self.__reference_flight_data_container:

            # try with no stopovers
            self.__new_flight_search = self.create_flight_search_obj(ref_destination, stop_overs=0)

            search_result = self.__new_flight_search.get_flight_data()

            try:

                # FlightSearch only returns 1 search result hence [0] index
                self.__destination_price_list.append(self.write_to_dict_nonstop(search_result["data"][0]))

            except IndexError:

                # try with 1 stopover
                new_flight_search = self.create_flight_search_obj(ref_destination, stop_overs=1)
                search_result = new_flight_search.get_flight_data()

                try:
                    route_list = []
                    for route in search_result["data"][0]["route"]:  # test for exception ... check if "route" list

                        # check if there is a route data available
                        if route:
                            route_list.append({
                                "cityCodeFrom": route["cityCodeFrom"],
                                "cityCodeTo": route["cityCodeTo"],
                                "cityFrom": route["cityFrom"],
                                "cityTo": route["cityTo"]
                            })

                    # FlightSearch only returns 1 search result hence [0] index
                    self.__destination_price_list.append(self.write_to_dict_stopover(search_result["data"][0],
                                                                                     route_list))

                except IndexError:
                    print(f"No available fight from {self.__current_location} to {ref_destination['city']}")

    def create_flight_search_obj(self, ref_destination, stop_overs):

        """
            Create new FlightSearch object to retrieve the latest flight data using Tequila API.
                Parameter:
                    ref_destination (DataManager): Reference flight prices and locations in which to search.
        """

        flight_search = FlightSearch(flight_from=self.__current_location,
                                     flight_to=ref_destination["iataCode"],
                                     week_range=self.__date_offset_in_week,
                                     price_to=ref_destination["lowestPrice"],
                                     min_return_time_days=self.__min_return_time_days,
                                     max_return_time_days=self.__max_return_time_days,
                                     stop_overs=stop_overs
                                     )

        return flight_search

    def write_to_dict_nonstop(self, destination):

        """
            Convert Flight data of interest in to dict for nonstop flights.
                Parameter:
                    destination (FlightSearch): FlightSearch data object for given reference destination.
                Returns:
                    fight_dict (dict): Dictionary containing flight data of interest pertaining to non_direct flights.
        """

        flight_dict = {"from_location": destination["cityFrom"],
                       "to_location": destination["cityTo"],
                       "from_IATA": destination["cityCodeFrom"],
                       "to_IATA": destination["cityCodeTo"],
                       "price": destination["price"],
                       "current_date": self.__new_flight_search.get_date(),
                       "offset_date": self.__new_flight_search.get_offset_date(),
                       "link": destination["deep_link"]
                       }

        return flight_dict

    def write_to_dict_stopover(self, destination, route_list):

        """
            Convert Flight data of interest in to dict for non-direct flights
                Parameter:
                    destination (FlightSearch): FlightSearch data object for given reference destination.
                    route_list (list): List of route dictionaries travelled through via non-direct flight.
                Returns:
                    fight_dict (dict): Dictionary containing flight data of interest pertaining to non-direct flights.
        """

        flight_dict = {"from_location": destination["cityFrom"],
                       "to_location": destination["cityTo"],
                       "from_IATA": destination["cityCodeFrom"],
                       "to_IATA": destination["cityCodeTo"],
                       "price": destination["price"],
                       "current_date": self.__new_flight_search.get_date(),
                       "offset_date": self.__new_flight_search.get_offset_date(),
                       "route": route_list,
                       "link": destination["deep_link"]
                       }
        return flight_dict

    def get_flight_data(self):

        """
            Get current flight data.
                Returns:
                    self.__destination_price_list (dict): Returns list of available flight deals.
        """

        return self.__destination_price_list

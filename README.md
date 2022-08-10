# Cheap_Flight_Finder_Python_2.0
Upgraded version of the “Cheap_Flight_Finder_Python”

Users register their name and email with the "Flight Club" app which saves their contact information to a Google Sheets document using the Sheety API.

The app finds the cheapest direct and single stopover non-direct flight deals online using kiwi.com and their Tequila API. The app searches a predetermined list of destinations stored as a Google Sheets document and accesses them using the Sheety API.

Destinations with no flight deals are printed to console. 

Flights are selected with a minimum trip duration of seven days and a maximum duration of thirty days.

If the app finds a flight that is cheaper than the historic lowest price for a certain destination, the app sends a customized email to registered users containing the user’s name, the route if it is a non-direct flight and a hyperlink to kiwi.com to book a flight.







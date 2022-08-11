# Cheap_Flight_Finder_Python_2.0
Upgraded version of the “Cheap_Flight_Finder_Python”

Users register their name and email with the "Flight Club" app (See Figure 1) which saves their contact information to a Google Sheets document using the Sheety API (See Figure 2).

The app finds the cheapest direct and single stopover non-direct flight deals online using kiwi.com and their Tequila API. The app searches a predetermined list of destinations stored as a Google Sheets document and accesses them using the Sheety API (See Figure 3)

Destinations with no flight deals are printed to console (See Figure 1). 

Flights are selected with a minimum trip duration of seven days and a maximum duration of thirty days.

If the app finds a flight that is cheaper than the historic lowest price for a certain destination, the app sends a customized email to registered users containing the user’s name, the flight route, the date and time of departure and return flights and a hyperlink to kiwi.com to book a flight (See Figure 4, 5, 6, 7).


For more info see the links below:

https://www.kiwi.com/en/

https://www.twilio.com

https://sheety.co

***

<img width="775" alt="image" src="https://user-images.githubusercontent.com/76194492/183819392-4f8928ac-c1ad-4b1c-bebc-52f81228331a.png">

Figure 1: Example of User registration.

***

![image](https://user-images.githubusercontent.com/76194492/183822884-2836fd34-a1ed-4a18-97db-49d364202d52.png)

Figure 2: User data stored within Google Sheets document.


***

![image](https://user-images.githubusercontent.com/76194492/183819523-1bb47068-fc44-4246-8792-5275ed7292af.png)

Figure 3: Reference destination list with lowest price stored within Google Sheets document.

***
![image](https://user-images.githubusercontent.com/76194492/183820300-c2f4047e-f78f-4fc7-83f2-0080960cc281.png)

Figure 4: Flight deal sample email.


***

<img width="1462" alt="image" src="https://user-images.githubusercontent.com/76194492/184047192-aeb05714-50d5-422b-aeb8-194dad020e0e.png">

Figure 5: Non-direct flight sample email. 

***

<img width="1462" alt="image" src="https://user-images.githubusercontent.com/76194492/184047169-93418c34-5fb5-43db-9205-bd43ddf9fe3a.png">

Figure 6: Direct flight sample email.  

***

![image](https://user-images.githubusercontent.com/76194492/183822524-cc746825-dc93-4f85-94b8-cb9e285da340.png)

Figure 7: Opened flight deal hyperlink sample.  

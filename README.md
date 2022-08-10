# Cheap_Flight_Finder_Python_2.0
Upgraded version of the “Cheap_Flight_Finder_Python”

Users register their name and email with the "Flight Club" app (See Figure 1) which saves their contact information to a Google Sheets document using the Sheety API (See Figure 2).

The app finds the cheapest direct and single stopover non-direct flight deals online using kiwi.com and their Tequila API. The app searches a predetermined list of destinations stored as a Google Sheets document and accesses them using the Sheety API (See Figure 3)

Destinations with no flight deals are printed to console (See Figure 1). 

Flights are selected with a minimum trip duration of seven days and a maximum duration of thirty days.

If the app finds a flight that is cheaper than the historic lowest price for a certain destination, the app sends a customized email to registered users containing the user’s name, the route if it is a non-direct flight and a hyperlink to kiwi.com to book a flight (See Figure 4, 5, 6).


For more info see the links below:

https://www.kiwi.com/en/

https://www.twilio.com

https://sheety.co

***

<img width="775" alt="image" src="https://user-images.githubusercontent.com/76194492/183819392-4f8928ac-c1ad-4b1c-bebc-52f81228331a.png">

Figure 1: Example of User registration.

***

![image](https://user-images.githubusercontent.com/76194492/183819721-7952681e-9111-40e5-913a-83451ccdbb6a.png)

Figure 2: User data stored within Google Sheets document.


***

![image](https://user-images.githubusercontent.com/76194492/183819523-1bb47068-fc44-4246-8792-5275ed7292af.png)

Figure 3: Reference destination list with lowest price stored within Google Sheets document.

***
![image](https://user-images.githubusercontent.com/76194492/183820300-c2f4047e-f78f-4fc7-83f2-0080960cc281.png)

Figure 4: Flight deal sample email.


***

![image](https://user-images.githubusercontent.com/76194492/183820001-bab189b6-3f6d-4d95-9c12-1aa8a9da18aa.png)

Figure 5: Non-direct flight sample email. 

***

![image](https://user-images.githubusercontent.com/76194492/183820472-c0f34e95-4f3f-4077-998b-c090b2fc6716.png)
Figure 6: Direct flight sample email.  


# Currency-Wikipedia-Scraper

Communication Contract:

How to request data (using ZeroMQ): 

1. Connect to tcp://localhost:3000.

![connect](https://user-images.githubusercontent.com/91433409/199150603-616d6ac2-98cd-47e3-a5e7-5337e4125ac7.PNG)

2. Send the currency code to the server as a string.

![send](https://user-images.githubusercontent.com/91433409/199150644-3e38f4ab-b0b2-4c44-aa99-275d8350c6cb.PNG)

How to receive data (using ZeroMQ): 

1. Receive the sentences as a string. 

![receive](https://user-images.githubusercontent.com/91433409/199150940-318e1473-c36c-4f5e-a3d0-5cb74bc54274.PNG)

example: ![sentence](https://user-images.githubusercontent.com/91433409/199151267-e32bd608-d4b7-4fdc-a103-cecf8d6fceb9.PNG)

UML Sequence Diagram: 

![easy](https://user-images.githubusercontent.com/91433409/199152690-6ca23501-c841-4d2d-ac94-1e3be96a2b15.PNG)

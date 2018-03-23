# Simple Distributed Blackboard

* A program that runs on several machines

* Clients post to any server using a web browser

* Store all received data

* Propagate the newly received data	

  * to all the other boards
  
  * in a peer-to-peer manner
  
## Communications between a client and any server

* HTTP requests

  * GET / -> display the page
  
  * GET /board -> display the content of the board (the data)
  
  * POST /board -> add a new value to the board
  
* HTTP Status

* We can inform the client upon a request

  * 200: OK

  * 400: Bad Request (But this should never happen!)
  
## Some hints

* Keep a list of all vessels in each vessel

* Upon a post

  * Send the update to all other vessels
  
  * But don’t wait for the other to reply before responding to the client!
  
  * Store the value, it should be shown at the next refresh
  
* HTTP formatting

  * Do not care how it looks as long it is usable

* The mininet script **lab1.py**  calls a python script called **server/server.py**

  * The script also provides the server IP as input to the script
  
## Task 1: Make it work https://youtu.be/R_g3SpWsUV8

* Demonstrate that the distributed blackboard works

* Use at least 8 vessels/blackboards

* Do 3 posts and show them on the other blackboards

## Task 2: Modify and Delete values https://youtu.be/ugkoNUJ0PDQ

* A user must be able to delete or modify a post

* Once a post is either modified or deleted, a vessel should propagate this change to other vessels

## Task 3: Is the system consistent? https://youtu.be/_OZzknPRXKo

* Can it happen that two vessels show different blackboards? Why?

* Even when all data was reliably send to all vessels, and then we hit refresh afterwards


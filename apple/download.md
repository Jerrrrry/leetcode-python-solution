I have implemented a similar system previously.

The request has the parameters like chunk number and max chunk size(optional) for the file. Initially, the chunk number would be 0.
The server splits a file based on the max chunk size and uses file offset to skip the max chunk size in bytes * chunk number bytes in the file and returns the next max chunk size to the client.
When the client receives the chunk, the client sends another request by incrementing the chunk number.
Continue this till you get the confirmation from the server that no data is left to send. Similar to the pagination logic.
Once all the data is received on the client-side, combine the chunks into one single file.
If there is a problem with the ith chunk number due to network failure, try the download again after x seconds or by the click of a retry button.
The high-level design would be the above explanation with some flow charts and UML diagrams.

The low-level design would be Interfaces, Classes, and its methods if you are going OOPs way or appropriate function declarations if you are going functional way. I guess you can come up with the classes and the methods which are capable of storing the state in properties and a method that can request the server and a method to combine everything.

Hope it helps.
# Python-Chat-Room

Sure, here is the updated README:

## Chat Room

This is a simple chat room application that can be used by multiple users to communicate with each other. The application is written in Python and uses the `socket` module to create a TCP server. The server listens for connections from clients and then sends them a welcome message. Once a client is connected, they can type messages to other clients. The server then broadcasts the messages to all other connected clients.

The application also supports a few simple commands. For example, the `:mytime` command will display the current time. The `:+1hr` command will display the current time + 1 hour. The `:Exit` command will close the client connection.

To use the application, first start the server by running the following command:

```
python3 server.py -start -port <port> -passcode <passcode>
```

Then, open a new terminal window and run the following command to connect to the server:

```
python3 client.py -join -host <hostname> -port <port> -username <username> -passcode <passcode>
```

You will be prompted to enter a display name and a passcode. The passcode is "12345" by default. Once you have entered your credentials, you will be connected to the chat room. You can then type messages to other clients.

To exit the chat room, type `:Exit` and press Enter.

## Files

The following files are included in the repository:

* `server.py`: The server program.
* `client.py`: The client program.
* `README.md`: This file.

## Running the Application

To run the application, first start the server by running the following command:

```
python3 server.py -start -port <port> -passcode <passcode>
```

Then, open a new terminal window and run the following command to connect to the server:

```
python3 client.py -join -host <hostname> -port <port> -username <username> -passcode <passcode>
```

You will be prompted to enter a display name and a passcode. The passcode is "12345" by default. Once you have entered your credentials, you will be connected to the chat room. You can then type messages to other clients.

To exit the chat room, type `:Exit` and press Enter.

## Commands

The application supports a few simple commands:

* `:mytime`: Displays the current time.
* `:+1hr`: Displays the current time + 1 hour.
* `:Exit`: Closes the client connection.

## Connection Establishment and Password Checking

When a client connects to the server, it must provide a username and a passcode. The server will then check the passcode against the one that was provided when the server was started. If the passcodes match, the client will be allowed to join the chat room. If the passcodes do not match, the client will be disconnected.

## Chat Functionality

Once a client has joined the chat room, they can type messages to other clients. The server will then broadcast the messages to all other connected clients.

## Chat Shortcuts

The application supports a few chat shortcuts:

* `:mytime`: Displays the current time.
* `:+1hr`: Displays the current time + 1 hour.
* `:Exit`: Closes the client connection.

## Leaving Chatroom

To leave the chat room, a client can type `:Exit`. The server will then disconnect the client.

## Troubleshooting

If you are having trouble running the application, please check the following:

* Make sure that you have Python 3 installed.
* Make sure that you are running the correct commands.
* Make sure that you are entering the correct credentials.

If you are still having trouble, please create an issue in the repository and I will try to help you.

import socket
import threading
import sys 
import datetime


#TODO: Implement all code for your server here

# Use sys.stdout.flush() after print statemtents



# server.py -start -port <port> -passcode <passcode>
port = int(sys.argv[3])
password = sys.argv[5]


host = '127.0.0.1' #local host

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", port)) #binds the server to the host and IP address
server.listen() #puts our server into listening mode for new connections

clients = []
usernames = []


#broadcasts message to all clients in curr client list
def broadcast(currClient, message):
	for client in clients:
		if client is not currClient:
			client.send(message)
	
#our message processing process 
def handle(client):
	while True:
		try:
			#when we receive a message from a client, we should immediately send this message to all the other clients
			message = client.recv(1024).decode('ascii')
			if ":Exit" in message:
				removeClient(client)
				break
			else:
				message = inputConvert(message)
				print(message)
				sys.stdout.flush()
				broadcast(client, message.encode('ascii'))
		except:
			break

def inputConvert(message):
	if ":)" in message:
		message = message.replace(":)", "[feeling happy]")
	elif ":(" in message:
		message = message.replace(":(", "[feeling sad]")
	elif ":mytime" in message:
		current_time = datetime.datetime.now()
		formatted_time = current_time.strftime("%a %b %d %H:%M:%S %Y")
		message = message.replace(":mytime", formatted_time)
	elif ":+1hr" in message:
		current_time = datetime.datetime.now()
		one_hour_later = current_time + datetime.timedelta(hours=1)
		formatted_time = one_hour_later.strftime("%a %b %d %H:%M:%S %Y")
		message = message.replace(":+1hr", formatted_time)
	return message
    
def removeClient(client):
	index = clients.index(client)
	clients.remove(client)
	nickname = usernames[index]
	goodbye_message = f'{nickname} left the chatroom'
	print(nickname + " left the chatroom")
	#print(goodbye_message.encode('ascii'))
	sys.stdout.flush()
	broadcast(client, f'{nickname} left the chatroom'.encode('ascii'))
	usernames.remove(nickname)
	clients.remove(client)
	client.close()
#main method that accepts all the connections
def receive():
	while True:
		#we are basically running server.accept all the time and if we get a suitable connection then the server.accept() method will 
		#accept this connection into the server
		client, address = server.accept()
		sys.stdout.flush()

		#Our nickname extraction process
		client.send('PASSWORD'.encode('ascii'))
		client_password = client.recv(1024).decode('ascii')
		if (client_password != password):
			client.send('PASSFAIL'.encode('ascii'))
			client.close()
		else:
			client.send('USERNAME'.encode('ascii'))
			username = client.recv(1024).decode('ascii')
			usernames.append(username)
			clients.append(client)
			welcomeMessage = f"{username} joined the chatroom".encode('ascii')
			print(welcomeMessage.decode('ascii'))
			sys.stdout.flush()
			broadcast(client, f"{username} joined the chatroom".encode('ascii'))
			client.send(f"Connected to {host} on port {port}".encode('ascii'))

			thread = threading.Thread(target = handle, args=(client,))
			thread.start()

if __name__ == "__main__":
	print(f"Server started on port {port}. Accepting connections")
	sys.stdout.flush()
	receive()
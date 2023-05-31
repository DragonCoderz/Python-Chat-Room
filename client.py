import socket
import threading
import sys 

#client.py -join -host <hostname> -port <port> -username <username> -passcode <passcode>
host = sys.argv[3]
port = int(sys.argv[5])
username = sys.argv[7]
passcode = sys.argv[9]


#TODO: Implement a client that connects to your server to chat with other clients here

# Use sys.stdout.flush() after print statemtents

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', port))

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == 'PASSWORD':
				client.send(passcode.encode('ascii'))
			elif message == 'PASSFAIL':
				print("Incorrect passcode")
				sys.stdout.flush()
				break
			elif message == 'USERNAME':
				client.send(username.encode('ascii'))
			else:
				print(message)
				sys.stdout.flush()
		except:
			print("An error occured")
			sys.stdout.flush()
			break

def write():
	while True:
		message = f'{username}: {input("")}'
		client.send(message.encode('ascii'))

# receiveThread = threading.Thread(target=receive)
# receiveThread.start()

# writeThread = threading.Thread(target=write)
# writeThread.start()

# def check_credentials(username, passcode):
# 	if len(username) > 8 or not username.isalnum():
# 		print("Invalid username")
# 		sys.stdout.flush()
# 		return False
    
#     # Check the length of the password and if it's alphanumeric
# 	if len(passcode) > 5 or not passcode.isalnum():
# 		print("Incorrect passcode")
		
# 		return False
# 	return True

if __name__ == "__main__":
	receiveThread = threading.Thread(target=receive)
	receiveThread.start()
	writeThread = threading.Thread(target=write)
	writeThread.start()
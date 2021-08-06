# GitHub Ready version
#
# LAST UPDATED:  2021-08-06
# 
# TESTED:   ...


# Python modules
import threading        # Multi-Threading [!]
import socket


# Defining host-address and PORT
host = 'XXX.X.X.X'  # Local Host,  (  IP address of the device / server machine )
port = XXXX      # Banned ports for example: 80 , and well-known / reserverd PORTS !

# Starting the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # For creating sockets

# BINDING the SERVER to the HOST's IP Address
server.bind((host, port))   # The server is bound to:   host IP, and host PORT
server.listen()     # Puts the server to listening mode for new connections (it's looking for incoming connections)


# Defining 2 empty lists:
clients = []        # For storing all Client connections
nicknames = []      # For storing all related Client nicknames


# Broadcast function: Sends a message to all the Clients which are currently connected to this server
def broadcast(message):     # For broadcasting messages FROM SERVER TO CLIENTS
    for client in clients:      # Getting all the clients
        client.send(message)    # Sending a message to ALL the clients

# Handling Client Connections:
def handle(client):
    while True:     # Starting as an Endless Loop
        try:        # (As long as it works without giving you an EXCEPTION or an ERROR, continue)
            message = client.recv(1024)     # Max message limit: 1024 bytes
            broadcast(message)      # Broadcasting the message to all the other Clients, including the Client who sent the message
        except:     # Handling EXCEPTIONS and ERRORS
            index = clients.index(client)   # We need this INDEX to remove the Client from the LIST and to remove IT's NICKNAME
            clients.remove(client)
            client.close()      # Close the connection to the Client
            nickname = nicknames[index]     # ' The nickname of this Client is the INDEX of "nicknames". '
            broadcast(f'{nickname} left the chat!'.encode('ascii'))     # Broadcast to ALL the OTHER CLIENTS, that THIS CLIENT has DISCONNECTED

            nicknames.remove(nickname)      # Removing the Client's nickname ( same INDEX as in the 'clients[]' list )
            break   # Leaving this Loop


# Defining the Receive method ( = MAIN Method)
def receive():
    while True:     # The Server is accepting all connections
        client, address = server.accept()   # If the METHOD GETS A CONNECTION, it returns the 'Client' and the 'Address' of the Client
        print(f"Connected with: {str(address)}")     # ( Printing with 'f' string type )

        # Before connecting to the server, the Client will be able to Pick a NICKNAME
        client.send('NICK'.encode('ascii'))     # This is only visible to that particular Client
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)  # Adding the chosen Nickname
        clients.append(client)      # Adding the Client connection

        print(f'Nickname of the client is: {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))   # For telling EVERY OTHER CLIENT that a new Client is connected
        client.send('Connected to the server!'.encode('ascii'))     # Telling the Client, that he/she is connected

        #   Sending the Client to the 'handle' function
        thread = threading.Thread(target=handle, args=(client))   # We are going to run one thread FOR EACH CLIENT (We have to process the data roughly at the same time)
        thread.start()

print("Server is listening...")
receive()
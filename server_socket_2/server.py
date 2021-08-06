# GitHub Ready version
#
# LAST UPDATED:  2021-08-06
# 
# TESTED:   ...


# Python Modules
import socket 
import threading    # To Divide the Task Processing between Clients


HEADER = 64     # Every time when a connection occurs: the first message from our client will be a HEADER
#The LENGTH of our message

# To run the server, we need a NETWORK PORT
PORT = XXXX     # A Default Port

SERVER = socket.gethostbyname(socket.gethostname())
# Instead of a Hardcoded Value:    "192.168._.__."
print("DEVICE-ADDRESS:", socket.gethostbyname)

ADDR = (SERVER, PORT)   # Address =     the IP of our server + the PORT the server is on
FORMAT = 'utf-8'        # A Constant FORMAT for DECODING
DISCONNECT_MESSAGE = "!DISCONNECT"  # The text for disconnections


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # What Type of IP address are accepting OR looking for (for specific connections) ?

server.bind(ADDR) # We are going to BIND our server to a specific IP ADDRESS + PORT
# If a Client connects to this ADDRESS, then we are going to "stream" the data to the Client


def handle_client(conn, addr):      # To Define a connection
    # This will handle all communication between the CLIENT and the SERVER
    print(f"[NEW CONNECTION] {addr} connected.")    # A connection has occured

    connected = True        # Is the Client connected ?
    while connected:        # While we receive information from the Client, execute THIS:
        msg_length = conn.recv(HEADER).decode(FORMAT)   # How many [HEADER] bytes do we want to receive from the client ?
        # WE WILL NOT PASS this line of code, until we get a message from THE CLIENT.

        if msg_length:      # IF we get a VALID MESSAGE (therefore its not "NON") from the CLIENT, we handle it
            msg_length = int(msg_length)    # Convert the DECODED STRING into an INTEGER (the length of the message)
            msg = conn.recv(msg_length).decode(FORMAT)  # The actual message (the value of our message)
            if msg == DISCONNECT_MESSAGE:   # when a Client disconnects, THIS handles it
                connected = False           # To avoid Duplicate Connections...

            print(f"[{addr}] {msg}")        # If we received a message, we are going to print it (the ADDRESS and the ACTUAL MESSAGE)
            
            # Sending Messages from the SERVER to the CLIENT:
            conn.send("Msg received".encode(FORMAT))    # Every time when a message is received, we give a response

    conn.close()        # We CLOSED the disconnection
        

def start():        # Before we start streaming data, we check the connections in "handle_client"
    server.listen()     # Server is "listening" for new connections
    print(f"[LISTENING] Server is listening on {SERVER}")   # THIS prints out the Server's IP and its PORT
    while True:     # This only stops if we kill the server or it crashes
        conn, addr = server.accept()    # A new connection will wait HERE

        thread = threading.Thread(target=handle_client, args=(conn, addr))  # a Python 3 feature
        # We are going to PASS the arguments (ARGS) to the client handler (HANDLE_CLIENT)

        thread.start()  # We are going to start the "thread" 

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")    # For printing out the amount of ACTIVE CONNECTIONS
        # 1 thread means 1 connection. Connection between 2 threads =   1 CONNECTION

print("[STARTING] server is starting...")
start()
# GitHub Ready version
#
# LAST UPDATED:  2021-08-06
# 
# TESTED:   ...


# Python Modules
import socket

HEADER = 64                             # Same as the Server's
PORT = XXXX                             # Same as the Server's
FORMAT = 'utf-8'                        # Same as the Server's
DISCONNECT_MESSAGE = "!DISCONNECT"      # A text shown for disconnections
SERVER = "XXX.XXX.X.XXX"                 # THE IP WE ARE TRYING TO CONNECT TO!
# The Server's IP address is inserted in here!  Example:  "192.168.1.26"

ADDR = (SERVER, PORT)       # The FULL Address of the server (with IP + PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Same purpose as the Server's
client.connect(ADDR)        # Instead of BINDING, we CONNECT to the given address!

def send(msg):      # The way of sending messages to the server.
    message = msg.encode(FORMAT)    # For converting client message to BYTES FORMAT (Encoding)
    msg_length = len(message)       
    send_length = str(msg_length).encode(FORMAT)    # Convert the LENGTH of the MESSAGE into BYTES FORMAT (Encoding)
    send_length += b' ' * (HEADER - len(send_length))   # Making sure that our message will be 64 BYTES LONG
    # Appending to the message until it reaches exactly 64 BYTES:
    # We add BLANK spaces.

    client.send(send_length)    # The Client sends the message length in BYTES FORMAT
    client.send(message)        # The Client sends the message in BYTES FORMAT
    print(client.recv(2048).decode(FORMAT))     # To print out the MESSAGE which we RECEIVED from the SERVER (in STRING format)

# THE MESSAGES WE SEND (to the server):
send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")

# THE DISCONNECTION MESSAGE WE SEND (to the server):
send(DISCONNECT_MESSAGE)

# (To reconnect to the server, run the Script again!)
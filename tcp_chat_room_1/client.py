# GitHub Ready version
#
# LAST UPDATED:  2021-08-06
# 
# TESTED:   ...


# Python modules
import socket
import threading 


# Defining Client's Nickname
nickname = input("Choose a nickname: ")


# To define a socket: 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# When this line is executed, the SERVER will trigger the 'ACCEPT' METHOD, and the Client is then connected to the server!
client.connect(('XXX.X.X.X', XXXX))    # Port: XXXX ?


# Recieve Data Thread:
def receive():
    while True: # Endless Loop
        try:        # We are trying to RECEIVE MESSAGES from the Server !
            message = client.recv(1024).decode('ascii')   # Message MAX length is 1024 bytes and we decode it to ASCII
            if message == 'NICK':   # IF we get the message from the Server "NICK", then this will run.
                client.send(nickname.encode('ascii'))   # We send the NICKNAME to the Server.
            else:       # If the message is other than NICKNAME, then the Server will Print the message.
                print(message)
        except:     # If message receiving is not working, we are going to close the connection.
            print('An error occurred!')
            client.close()  # Disconnection
            break # In this case, we will end the Endless Loop

# Write Messages Data Thread:
def write():
    while True: # Endless Loop
        message = f'{nickname}: {input("")}'    # Always defining a new message, waiting for a new message  |  (chat function)

        # SENDING the Message (With encoding)
        client.send(message.encode('ascii'))
        

# Running the 'Receive' thread and the 'Write' thread:
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
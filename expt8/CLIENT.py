import socket 
# create a socket, with AF_INET : Address from the internet
# AF_INET accepts two params : host address and port number
# SOCK_STREAM used to create TCP protocols
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# using the localhost and the port number allowed on the server
# open a connection to the port on that address
s.connect((socket.gethostname(), 1025)) # connect to the server port

full_message = ''
# limit on the number of bytes read from the server at a time
n_bytes = 6 

while True:
    msg = s.recv(n_bytes) # message received, with limit on socket
    print(msg.decode('utf-8'), len(msg)) # print the information received
    full_message += msg.decode('utf-8') # append to the full_message
    if len(msg) < n_bytes :
        break # close the connection, once the message is received

print(full_message)
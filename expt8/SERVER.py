import socket
# create a socket, with AF_INET : Address from the internet
# AF_INET accepts two params : host address and port number
# SOCK_STREAM used to create TCP protocols
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# gethostname is used when client and server are on the same device
# bind the server to the client 
s.bind((socket.gethostname(), 1025)) # >1023  ---->  Non - privilege address
# Enter the listening mode
s.listen(5)
# for every connection
while True :
    clt,addr = s.accept()
    print(f'Connection to {addr} established!')
    # pass a message to the connected client
    clt.send(bytes('Socket programming in python!','utf-8'))
    clt.close()
    # end the connection and keep listening
# python socket server
import socket

# create a socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)# default protocol 0
# local hostname
host = socket.gethostname()
print("hostname: ",host)
# port
port = 8080
# bind to port
s.bind((host,port))
# listen to 3 requests at the same time
s.listen(3)
print("Listening...")
while True:
    # conncetion
    client,addr = s.accept()
    print("Connected to: ", addr)
    # receive from clienr
    msg = client.recv(1024)
    print(msg.decode('utf-8'))
    # send mesage to client
    data = "Hello,I am Server..."
    client.send(data.encode('utf-8'))
    # close connection
    client.close()
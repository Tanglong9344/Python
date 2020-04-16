import socket

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# local hostname
host = socket.gethostname()
print("hostname: ", host)
# port
port = 8080
# connection
s.connect((host, port))
# send message to server
data = "Hello,I am a client..."
s.send(data.encode('utf-8'))
# receive message from server
msg = s.recv(1024)
# close
s.close()
# print message
print(msg.decode('utf-8'))

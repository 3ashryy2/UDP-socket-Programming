from socket import *
serverPort = 10000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
while True:
  message, clientAddress = serverSocket.recvfrom(2048)
  newMessage = message.upper()
  serverSocket.sendto(newMessage, clientAddress)
  print( "message : ",message.decode(),"Client address : ",clientAddress)

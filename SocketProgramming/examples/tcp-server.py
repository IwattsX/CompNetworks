'''

TCP Server

'''

from socket import *

serverPort = 15000

serverSocket = socket()
# serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(2)

print('The server is ready to receive...')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()


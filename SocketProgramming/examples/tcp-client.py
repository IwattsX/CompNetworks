'''

TCP Client

'''

from socket import *

serverName = 'localhost'
serverPort = 15000

clientSocket = socket()
# clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

sentence = input('Enter lowercase sentence: ')

clientSocket.send(sentence.encode())  # We don't need to specify address (e.g. sendto)

modifiedSentence = clientSocket.recv(1024)

print(f'From server: {modifiedSentence.decode()}')

clientSocket.close()


from socket import *

serverName = 'localhost'
serverPort = 15000

clientSocket = socket()
# clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

while True:
    Math_input = input('Enter a mathematical expression: ')
    try:
        clientSocket.send(Math_input.encode())  # We don't need to specify address (e.g. sendto)
        Math_output = clientSocket.recv(1024)
        print(f'From server: {Math_output.decode()}')
    except BrokenPipeError:
        print("Server closed the connection.")
        break

clientSocket.close()

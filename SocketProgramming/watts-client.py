"""
Name: Isaac Watts
Date: 04/25/2024
Description: Socket programming from the client side with TCP

"""
from socket import *

serverName = 'localhost'

# Specifying the port, this will the same for the client
serverPort = 15000

clientSocket = socket()
# clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to a port and localhost on this machine
clientSocket.connect((serverName,serverPort))

Math_input = input('Enter a mathematical expression: ')
try:
    #Send the request to the server
    clientSocket.send(Math_input.encode())

    # Get the output from the server
    Math_output = clientSocket.recv(1024)

    # Decode the output from the server
    print(f'From server: {Math_output.decode()}')

except BrokenPipeError: # Detect if the server closed the connection
    print("Server closed the connection.")
finally:
    # Close the client socket
    clientSocket.close()

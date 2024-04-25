"""
Name: Isaac Watts
Date: 04/25/2024
Description: Socket programming from the server side with TCP

"""


from socket import *

serverPort = 15000


# Create an instance of a socket
serverSocket = socket()

# Assigning a port to the socket
serverSocket.bind(('', serverPort))


# Ready to listen to client request after listen(2)
serverSocket.listen(2)

print('The server is ready to receive...')

try:
    while True:
        # Accept the connection
        connectionSocket, addr = serverSocket.accept()
        print(f"Receiving from address {addr}")

        # Recieve the math expression from the client and decode it
        mathExpression = connectionSocket.recv(1024).decode()
        try:
            # Using python in built eval function to evaluate the math in the string
            answer = eval(mathExpression)

            # Send the server answer back to the client
            connectionSocket.send(str(answer).encode())

        except:  # noqa: E722 "No bare except", but we need to catch the case where the user sends something other than an expression to evaluate
            connectionSocket.send("Error in processing this expression. Is it a simple mathematical expression?".encode())
        finally:
            # Close the connection
            connectionSocket.close()

except KeyboardInterrupt:
    print("Server terminated")
    # Close the server socket
    serverSocket.close()

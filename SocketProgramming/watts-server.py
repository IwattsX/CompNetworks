from socket import *

serverPort = 15000

serverSocket = socket()
serverSocket.bind(('', serverPort))
serverSocket.listen(2)

print('The server is ready to receive...')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Receiving from address {addr}")
    mathExpression = connectionSocket.recv(1024).decode()
    try:
        answer = eval(mathExpression)
        connectionSocket.send(str(answer).encode())
    except:
        connectionSocket.send("Error in processing this expression. Is it a simple mathematical expression?".encode())
    finally:
        connectionSocket.close()

import socket

HOST_SERVER = '127.0.0.1'
PORT = 12000

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    socket_client.connect((HOST_SERVER, PORT))

    temperature = input('Enter the temperature in Celsius: ')

    socket_client.send(temperature.encode('utf-8'))

    response = socket_client.recv(1024).decode('utf-8')

    print(f'Server response: {response}')

except ConnectionRefusedError:
    print(f'Could not connect to the server at {HOST_SERVER}:{PORT}. Please ensure the server is running.')

finally:
    socket_client.close()        
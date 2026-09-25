import socket

HOST = '127.0.0.1'
PORT = 12000

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind((HOST, PORT))

socket_server.listen(1)
print(f'Server is listening on {HOST}:{PORT}...')
print(f'Waiting for a connection...')

while True:

    conection, address = socket_server.accept()
    print(f'Connection established with {address[0]}:{address[1]}')

    data = conection.recv(1024).decode('utf-8')

    if data:

        temperature = float(data)
        print(f'Received temperature: {temperature}°C')

        faranheit = (temperature * 1.8) + 32

        response = f'Faranheit: {faranheit}°F'

    conection.send(response.encode('utf-8'))

    conection.close()

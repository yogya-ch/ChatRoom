import socket
import select #OS Level monitoring operations

BUFFER = 1024
IP = "127.0.0.1" #Locat Host
PORT = 1234

#Socket SetUp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#To Avoid socket already in use error
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Binding IP and PORT
server_socket.bind((IP, PORT))
#Listening
server_socket.listen()
#list of sockets for select to keep track of
sockets_list = [server_socket]
print(f'Listening for connections on {IP}:{PORT}...')

def request_handler(client_socket):
    try:
        message_header = client_socket.recv(BUFFER)
        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except Exception as e:
        print(e)

        return False

while True:
    pass

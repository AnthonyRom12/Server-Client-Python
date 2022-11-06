import json
import socket

from server_operation import Server

server = Server()
db = ''
HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()  # socket obj

    with connection:
        print(f"Connected be: {address[0]} | {address[1]}")

        # Server command
        while True:
            key = server.recv_msg(connection)
            try:
                handler = server.handlers[key](conn=connection)
            except KeyError:
                server.send_msg(connection, f'Unsupported command: "{key}"')
                break
            except IndexError:
                server.send_msg(connection, f'Unsupported data format for command: "{key}"')
                break
            if key == "stop":
                break

            key, value = handler[0], handler[1]
            msg = json.dumps({key: value}, indent=2)
            server.send_msg(connection, msg)


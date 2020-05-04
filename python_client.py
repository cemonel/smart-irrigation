#!/usr/bin/env python
import socket


class PythonServer:

    def __init__(self, port, host):
        self.port = port
        self.host = host
        self.socket = socket.socket()
        self.socket.bind((port, host))

    def listen(self):
        self.socket.listen(2)
        conn, address = self.socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                break
            print("Coming data: " + str(data))

        conn.close()  # close the connection

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.port, self.host))

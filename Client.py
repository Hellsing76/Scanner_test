import urllib.parse
import urllib.request
import sys
import socket

import re

def Main():
        host = "67.222.1.194"
        port = 80

        mysocket = socket.socket()
        mysocket.connect((host, port))

        message = input("->")

        while message != 'q':
            mysocket.send(message.encode())
            data = mysocket.recv(2000).decode()

            print('This is your balance: ' + data)

            message = input("->")
        mysocket.close()


        if __name__ =='__main__':
            Main()


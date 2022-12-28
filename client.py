# rasbery pi üzerinde çalışacak python kodu

import socket

HEADER = 64
PORT = 9999
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "BAĞLANTI KESİLDİ"
IP = "35.184.74.35"
ADDR = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_lenth = str(len(message)).encode(FORMAT)
    header = msg_lenth + b' ' * (HEADER - len(msg_lenth))
    client.send(header)
    client.send(message)


while True:
    a = input()
    send(a)

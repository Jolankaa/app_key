# lavender app deprem rasbery pi derprem verisi göndermek için yazılmış bi program 
# author : jolanka github.com/jolankaa

import socket
import asyncio

HEADER = 64
IP = "35.184.74.35"
PORT = 9999
ADDR = (IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "TCP BAĞLANTI HATASI"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.setblocking(False)


async def handle_client(conn, addr):
    print(f"[SUNUCU BAĞLAMA] {addr} BAĞLANILIYOR...")
    loop = asyncio.get_event_loop()
    connected = True
    while connected:
        max_lenth = await loop.sock_recv(conn, HEADER)
        max_lenth = max_lenth.decode(FORMAT)
        if max_lenth:
            max_lenth = int(max_lenth)
            msg = await loop.sock_recv(conn, max_lenth)
            msg = msg.decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                print("[BAĞLANTI KESİLDİ]")
                connected = False

            print(f"[{addr}] -> {msg}")
            # Do whatever you want with message
            print(f"{len(asyncio.all_tasks())}")
        else:
            print(
                f"CLİENTİN BAĞLANTISI KESİLDİ {addr}")
            connected = False

    conn.close()


async def start():
    server.listen()
    print(f"[İP DİNLENİLİYOR] {IP}")
    loop = asyncio.get_event_loop()

    while True:
        conn, addr = await loop.sock_accept(server)
        loop.create_task(handle_client(conn, addr))


if __name__ == "__main__":
    print("[BAŞLATILIYOR] BEKLEYİN ...")
    asyncio.run(start())

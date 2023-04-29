import threading
import queue
import socket
from sys import argv

M = int(argv[1])
filename = argv[2]
list_of_urls = []


def connect_with_server(url):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(("localhost", 15000))

    client_sock.send(url.encode('UTF-8'))

    top_k = client_sock.recv(1024).decode()
    if top_k:
        print(f'{url}: {top_k}')
    else:
        print('No top')

    client_sock.close()


with open(filename, "r") as f:
    for line in f:
        list_of_urls.append(line)

for url in list_of_urls:
    threads = [
        threading.Thread(
            target=connect_with_server,
            name=f"class_thread_{i}",
            args=(url,)
        )
        for i in range(M)
]

for th in threads:
    th.start()

for th in threads:
    th.join()

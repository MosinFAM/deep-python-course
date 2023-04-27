import threading
import queue
import socket
from sys import argv

M = int(argv[1])


def send_to_server(url):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(("127.0.0.1", 5000))

    client_sock.send(url.encode('UTF-8'))

    top_k = client_sock.recv(1024).decode()
    if top_k:
        print(f'{url}: {top_k}')
    else:
        print('No top')

    client_sock.close()


list_of_urls = []

with open('urls.txt', "r") as f:
    for line in f:
        list_of_urls.append(line)

for url in list_of_urls:
    threads = [
        threading.Thread(
            target=send_to_server,
            name=f"class_thread_{i}",
            args=(url,)
        )
        for i in range(M)
]

for th in threads:
    th.start()

for th in threads:
    th.join()

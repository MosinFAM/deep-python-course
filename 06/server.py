import queue
import threading
import requests
import socket
from sys import argv
from bs4 import BeautifulSoup
from collections import OrderedDict

w, k = int(argv[2]), int(argv[4])
q = queue.Queue()


def master():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(("localhost", 15000))

    server_sock.listen(2)
    while True:
        client_sock, addr = server_sock.accept()
        q.put(client_sock)


def worker():
    while True:
        client_socket = q.get()
        url = client_socket.recv(1024).decode()
        fetch_url(url, sem)
        client_socket.close()
        print("Closed connection with client")
        q.task_done()


def fetch_url(client_sock):
    th = threading.current_thread()

    with sem:
        url = client_sock.recv(1024).decode()
        response = requests.get(url)
        html = response.text
        freq = counter(html)
        sorted_pairs = sorted(((key, value) for d in freq for key, value in d.items()), key=lambda pair: pair[1], reverse=True)
        top_k = OrderedDict()
        for key, value in sorted_pairs:
            if key not in top_k:
                top_k[key] = value
                if len(top_k) == 3:
                    break
        client_sock.send(top_k.encode())


def counter(html):
    soup = BeautifulSoup(html, "html.parser")
    text = " ".join(p.text for p in soup.find_all("p"))
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
    return freq


sem = threading.Semaphore(2)

threads = [
    threading.Thread(
        target=fetch_url,
        name=f"class_thread_{i}",
        args=(q, sem)
    )
    for i in range(w)
]

for th in threads:
    th.start()

for th in threads:
    th.join()

q.join()

w, k = int(argv[3]), int(argv[5])


master_th = threading.Thread(target=master(), name="class_thread_01", args=())
master_th.start()

import queue
import threading
import json
import socket
from sys import argv
from bs4 import BeautifulSoup
from urllib.request import urlopen

# print(argv)
w, k = int(argv[2]), int(argv[4])
queue_of_urls = queue.Queue()


def master():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(("localhost", 15000))

    server_sock.listen(2)
    while True:
        client_sock, addr = server_sock.accept()
        queue_of_urls.put(client_sock)


def worker():
    while True:
        client_socket = queue_of_urls.get()
        urls = client_socket.recv(1024).decode()
        fetch_url(urls)
        client_socket.close()
        queue_of_urls.task_done()


def fetch_url(client_sock):
    url = urlopen(client_sock.recv(1024).decode())
    a = url.read()
    res_html = a.decode("utf-8")
    freq = counter(res_html)
    temp_top_k = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]
    top_k = json.dumps(dict(temp_top_k))

    return top_k


def fetch_several_urls(q):
    while True:
        try:
            url = q.get_nowait()
        except Exception:
            return
        q.task_done()

        fetch_url(url)


def counter(html):
    soup = BeautifulSoup(html, "html.parser")
    text = " ".join(p.text for p in soup.find_all("p"))
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
    return freq


master_thread = threading.Thread(target=master(), name="class_thread_01", args=())
master_thread.start()
master_thread.join()

worker_threads = [
    threading.Thread(
        target=fetch_url,
        name=f"class_thread_{i}",
        args=(queue_of_urls,),
        daemon=True
    )
    for i in range(w)
]

for th in worker_threads:
    th.start()

for th in worker_threads:
    th.join()

queue_of_urls.join()

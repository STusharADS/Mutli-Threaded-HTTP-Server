import concurrent.futures
import sys
import os
import socket
from collections import deque
import time
import json
from email.utils import formatdate
import threading
from urllib.parse import unquote

port = 8080
interface = "127.0.0.1"
resources = "resources"

def start_server(port, interface, resource_dir, maxPoolSize=10):
    global no_of_clients
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((interface, port))
    sock.listen()
    with concurrent.futures.ThreadPoolExecutor(max_workers=maxPoolSize) as executor:
        while True:
            conn, addr = sock.accept()
            conn.settimeout(30)
            lock.acquire()
            no_of_clients+=1
            if no_of_clients >= maxPoolSize:
                print("Thread pool saturated, queing connection")
                client_que.append((conn, addr))
            else:
                executor.submit(handle_client_connection, conn, addr, executor, resource_dir)
            lock.release()


if __name__ == "__main__":
    PORT = port
    INTERFACE = interface
    threadpool_size = 10
    if len(sys.argv) >= 2:
        try:
            PORT = int(sys.argv[1])
        except:
            print(f"Invalid port: {sys.argv[1]}")
        if len(sys.argv) >= 3:
            INTERFACE = str(sys.argv[2])
        if len(sys.argv) >= 4:
            threadpool_size = int(sys.argv[3])
    
    base_dir = os.path.dirname(os.path.realpath(__file__))
    resource_dir = os.path.join(base_dir, resources)

    # start_server(PORT, INTERFACE, resource_dir, threadpool_size)


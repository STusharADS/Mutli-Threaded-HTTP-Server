
import sys
import os

port = 8080
interface = "127.0.0.1"
resources = "resources"

if __name__ == "__main__":
    PORT = port
    INTERFACE = interface
    threadpool_size = 10
    # sys.argv takes input from command line
    # sys.argv[0] is reserved for file name (e.g. server.py)
    if len(sys.argv) >= 2:
        try:
            PORT = int(sys.argv[1])
        except:
            print(f"Invalid port Number. Using Default {PORT}")
        if len(sys.argv) >= 3:
            INTERFACE = str(sys.argv[2])
        if len(sys.argv) >= 4:
            threadpool_size = int(sys.argv[3])
    
    base_dir = os.path.dirname(os.path.realpath(__file__))
    resource_dir = os.path.join(base_dir, resources)

    # start_server(PORT, INTERFACE, resource_dir, threadpool_size)


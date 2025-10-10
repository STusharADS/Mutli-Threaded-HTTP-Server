Python Multi-Threaded HTTP Server
This project provides a lightweight, multi-threaded HTTP server implemented in Python. It is designed to handle concurrent GET and POST requests efficiently. The server can serve a variety of static files (HTML, text, images) and includes an endpoint for uploading JSON data.

Core Features
Static File Serving: Handles GET requests for HTML, TXT, PNG, and JPEG files, including support for large file transfers.

JSON Data Upload: Accepts POST requests to a dedicated /upload endpoint to store JSON data securely.

Concurrent Processing: Utilizes a ThreadPoolExecutor to manage multiple client connections simultaneously, with a queuing system for requests that exceed the pool size.

Secure by Design: Implements path resolution checks to prevent directory traversal attacks and ensures uploads are stored in a designated directory.

Standards-Compliant: Responds with proper HTTP status codes and headers.

Configurable: Allows command-line configuration of the server port, interface, and thread pool size.

Project Structure
project/
├── server.py
├── README.md
├── resources/
│   ├── index.html
│   ├── about.html
│   ├── ... (other static files)
│   └── sample_post.json
└── uploads/
Getting Started
Prerequisites:

Python 3.8 or newer

Running the Server:
Launch the server from your terminal using the following command:

Bash

python3 server.py [PORT] [INTERFACE] [THREADPOOL_SIZE]
PORT: (Optional) The port to listen on. Defaults to 8080.

INTERFACE: (Optional) The network interface to bind to. Defaults to 127.0.0.1.

THREADPOOL_SIZE: (Optional) The number of worker threads. Defaults to 10.

Example:

Bash

python3 server.py 8080 127.0.0.1 10
API Endpoints
1. GET /<file_path>
Serves static files located in the resources/ directory.

Example (HTML):

Bash

curl http://127.0.0.1:8080/index.html
Example (Image):

Bash

curl http://127.0.0.1:8080/Meme.png --output my_meme.png
2. POST /upload
Uploads JSON data to the server. The data is saved as a new file in the uploads/ directory.

Headers: Content-Type: application/json

Example (curl):

Bash

curl -X POST http://127.0.0.1:8080/upload \
     -H "Content-Type: application/json" \
     -d @resources/sample_post.json
Success Response:

JSON

{
  "status": "success",
  "message": "File created successfully",
  "filepath": "/uploads/upload_1727522345.json"
}
Implementation Highlights
Concurrency: Client connections are handled by a ThreadPoolExecutor for efficient, non-blocking I/O.

Thread Safety: A deque and threading.Lock are used to safely queue and manage connections when the thread pool is at capacity.

Security: os.path.realpath is used to resolve and validate file paths, preventing access to files outside the designated resources directory.

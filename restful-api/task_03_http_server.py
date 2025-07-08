from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json

HOST = "localhost"
PORT = 8000


class Handler(BaseHTTPRequestHandler):
    """
        Handler subclass of BaseHTTPRequestHandler
        handling requests to paths
    """
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!") #sends response as bytes

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            response_dataset = {"name": "John", "age": 30, "city": "New York"}

            self.wfile.write(json.dumps(response_dataset).encode()) #converts a string to byte

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"OK")
        
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Endpoint not found")

server = HTTPServer((HOST, PORT), Handler)
server.serve_forever()
server.serve_close()

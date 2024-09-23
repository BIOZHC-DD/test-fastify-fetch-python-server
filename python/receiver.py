from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import socket

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            json_data = json.loads(post_data.decode('utf-8'))
            print("Received JSON message:", json_data)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Message received successfully")
        except json.JSONDecodeError:
            print("Error: Invalid JSON received")
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Error: Invalid JSON")

def run_server(port=8000):
    server_address = ('', port)
    while True:
        try:
            httpd = HTTPServer(server_address, RequestHandler)
            print(f"Python server running on port {port}")
            httpd.serve_forever()
        except OSError as e:
            if e.errno == 48:  # Address already in use
                print(f"Port {port} is already in use. Trying the next port...")
                port += 1
                server_address = ('', port)
            else:
                raise  # Re-raise the exception if it's not about the address being in use

if __name__ == '__main__':
    run_server()

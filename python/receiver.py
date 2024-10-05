#from http.server import HTTPServer, BaseHTTPRequestHandler
#import json
#import socket
#import requests
#import threading
#
#class RequestHandler(BaseHTTPRequestHandler):
#    def do_POST(self):
#        content_length = int(self.headers['Content-Length'])
#        post_data = self.rfile.read(content_length)
#        
#        try:
#            json_data = json.loads(post_data.decode('utf-8'))
#            print("Received JSON message:", json_data)
#            
#            self.send_response(200)
#            self.send_header('Content-type', 'text/plain')
#            self.end_headers()
#            self.wfile.write(b"Message received successfully")
#        except json.JSONDecodeError:
#            print("Error: Invalid JSON received")
#            self.send_response(400)
#            self.send_header('Content-type', 'text/plain')
#            self.end_headers()
#            self.wfile.write(b"Error: Invalid JSON")
#
#def run_server(port=8000):
#    server_address = ('', port)
#    while True:
#        try:
#            httpd = HTTPServer(server_address, RequestHandler)
#            print(f"Python server running on port {port}")
#            httpd.serve_forever()
#        except OSError as e:
#            if e.errno == 48:  # Address already in use
#                print(f"Port {port} is already in use. Trying the next port...")
#                port += 1
#                server_address = ('', port)
#            else:
#                raise  # Re-raise the exception if it's not about the address being in use
#
#def send_message_to_node():
#    while True:
#        key = input("Press 'e' to send a message to the Node server: ")
#        if key.lower() == 'e':
#            try:
#                response = requests.post('http://localhost:3000/api/log', json={'message': 'Message from Python server'})
#                print(f"Message sent to Node server. Response: {response.text}")
#            except requests.RequestException as e:
#                print(f"Error sending message to Node server: {e}")
#
#
##if __name__ == '__main__':
##    run_server()
#
#
#
#if __name__ == '__main__':
#    # Start the HTTP server in a separate thread
#    server_thread = threading.Thread(target=run_server)
#    server_thread.start()
#
#    # Start the input loop in the main thread
#    send_message_to_node()



#from http.server import HTTPServer, BaseHTTPRequestHandler
#import json
#import socket
#import requests
#import threading
#
#class RequestHandler(BaseHTTPRequestHandler):
#    def do_POST(self):
#        content_length = int(self.headers['Content-Length'])
#        post_data = self.rfile.read(content_length)
#        
#        try:
#            json_data = json.loads(post_data.decode('utf-8'))
#            print("Received JSON message:", json_data)
#            
#            self.send_response(200)
#            self.send_header('Content-type', 'text/plain')
#            self.end_headers()
#            self.wfile.write(b"Message received successfully")
#        except json.JSONDecodeError:
#            print("Error: Invalid JSON received")
#            self.send_response(400)
#            self.send_header('Content-type', 'text/plain')
#            self.end_headers()
#            self.wfile.write(b"Error: Invalid JSON")
#
#def run_server(port=8000):
#    server_address = ('', port)
#    while True:
#        try:
#            httpd = HTTPServer(server_address, RequestHandler)
#            print(f"Python server running on port {port}")
#            httpd.serve_forever()
#        except OSError as e:
#            if e.errno == 48:  # Address already in use
#                print(f"Port {port} is already in use. Trying the next port...")
#                port += 1
#                server_address = ('', port)
#            else:
#                raise  # Re-raise the exception if it's not about the address being in use
#
##def send_message_to_node():
##    while True:
##        key = input("Press 'e' to send a message to the Node server, or any other key to stop: ")
##        if key.lower() == 'e':
##            try:
##                response = requests.post('http://localhost:3000/api/log', json={'message': 'Message from Python server'})
##                print(f"Message sent to Node server. Response: {response.text}")
##            except requests.RequestException as e:
##                print(f"Error sending message to Node server: {e}")
##        else:
##            print("Stopping message sending.")
##            break
#
#def send_message_to_node():
#    while True:
#        message = input("Enter your message to send to the Node server (or type 'quit' to stop): ")
#        if message.lower() == 'quit':
#            print("Stopping message sending.")
#            break
#        try:
#            response = requests.post('http://localhost:3000/api/log', json={'message': message})
#            print(f"Message sent to Node server. Response: {response.text}")
#        except requests.RequestException as e:
#            print(f"Error sending message to Node server: {e}")
#
#if __name__ == '__main__':
#    # Start the HTTP server in a separate thread
#    server_thread = threading.Thread(target=run_server)
#    server_thread.start()
#    
#    # Start the input loop in the main thread
##    send_message_to_node()
#    
#    # After send_message_to_node() exits, we can optionally clean up
##    print("Exiting the program.")
#    # You might want to add code here to stop the server thread if needed



#from http.server import HTTPServer, BaseHTTPRequestHandler
#import json
#import requests
#
#class RequestHandler(BaseHTTPRequestHandler):
#    def do_POST(self):
#        content_length = int(self.headers['Content-Length'])
#        post_data = self.rfile.read(content_length)
#        
#        try:
#            json_data = json.loads(post_data.decode('utf-8'))
#            print("Received JSON message:", json_data)
#            
#            # Send the received message to the Node server
#            response = requests.post('http://localhost:3000/api/log', json=json_data)
#            print(f"Message sent to Node server. Response: {response.text}")
#            
#            self.send_response(200)
#            self.send_header('Content-type', 'text/plain')
#            self.end_headers()
#            self.wfile.write(b"response from the python server")
#        except json.JSONDecodeError:
#            print("Error: Invalid JSON received")
#            self.send_response(400)
#            self.send_header('Content-type', 'text/plain')
#            self.end_headers()
#            self.wfile.write(b"Error: Invalid JSON")
#        except requests.RequestException as e:
#            print(f"Error sending message to Node server: {e}")
#            self.send_response(500)
#            self.send_header('Content-type', 'text/plain')
#            self.end_headers()
#            self.wfile.write(b"Error: Failed to forward message to Node server")
#
#def run_server(port=8000):
#    server_address = ('', port)
#    httpd = HTTPServer(server_address, RequestHandler)
#    print(f"Python server running on port {port}")
#    httpd.serve_forever()
#
#if __name__ == '__main__':
#    run_server()



#from http.server import HTTPServer, BaseHTTPRequestHandler
#import json
#import requests
#
#class RequestHandler(BaseHTTPRequestHandler):
#    def do_POST(self):
#        content_length = int(self.headers['Content-Length'])
#        post_data = self.rfile.read(content_length)
#        
#        try:
#            json_data = json.loads(post_data.decode('utf-8'))
#            print("Received JSON message:", json_data)
#            
#            # Send a one-line response to the Node server
#            response = requests.post('http://localhost:3000/api/log', data="Message received by Python server")
#            print(f"One-line message sent to Node server. Response: {response.text}")
#            
#            self.send_response(200)
#            self.send_header('Content-type', 'text/plain')
#            self.end_headers()
#            self.wfile.write(b"Message forwarded to Node server")
#        except json.JSONDecodeError:
#            print("Error: Invalid JSON received")
#            self.send_response(400)
#            self.send_header('Content-type', 'text/plain')
#            self.end_headers()
#            self.wfile.write(b"Error: Invalid JSON")
#        except requests.RequestException as e:
#            print(f"Error sending message to Node server: {e}")
#            self.send_response(500)
#            self.send_header('Content-type', 'text/plain')
#            self.end_headers()
#            self.wfile.write(b"Error: Failed to forward message to Node server")
#
#def run_server(port=8000):
#    server_address = ('', port)
#    httpd = HTTPServer(server_address, RequestHandler)
#    print(f"Python server running on port {port}")
#    httpd.serve_forever()
#
#if __name__ == '__main__':
#    run_server()


from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import requests

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            json_data = json.loads(post_data.decode('utf-8'))
            print("Received JSON message:", json_data)
            
            # Send a one-line JSON response to the Node server
            response_data = {"message": "Message received by Python server"}
            response = requests.post('http://localhost:3000/api/log', json=response_data)
            print(f"JSON message sent to Node server. Response: {response.text}")
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "Message forwarded to Node server"}).encode('utf-8'))
        except json.JSONDecodeError:
            print("Error: Invalid JSON received")
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode('utf-8'))
        except requests.RequestException as e:
            print(f"Error sending message to Node server: {e}")
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Failed to forward message to Node server"}).encode('utf-8'))

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Python server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()

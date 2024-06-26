import http.server
import json

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                'name': 'John',
                'age': 30,
                'city': 'New York'
            }
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status_data = {'status': 'OK'}
            self.wfile.write(json.dumps(status_data).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

def main():
    host = 'localhost'
    port = 8000
    server_address = (host, port)
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)
    print(f'Starting server on {host}:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    main()

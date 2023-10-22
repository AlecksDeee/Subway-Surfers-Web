import http.server
import socketserver
port = 8000
with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"The server started successfully at http://localhost:{port}")
    httpd.serve_forever()
